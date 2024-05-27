import numpy as np
import plotly.graph_objects as go

class Neuron:
    def __init__(self, n_inputs, bias = 0., weights = None):
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b)


class NeuralNetwork:
    def __init__(self):
        # Input layer with 3 neurons
        self.input_layer = [Neuron(n_inputs=3) for _ in range(3)]

        # Hidden layer 1 with 4 neurons
        self.hidden_layer1 = [Neuron(n_inputs=3) for _ in range(4)]

        # Hidden layer 2 with 4 neurons
        self.hidden_layer2 = [Neuron(n_inputs=4) for _ in range(4)]

        # Output layer with 1 neuron
        self.output_layer = Neuron(n_inputs=4)

    def forward(self, inputs):
        # Pass inputs through the input layer
        input_activations = np.array([neuron(inputs) for neuron in self.input_layer])

        # Pass activations through the first hidden layer
        hidden_activations1 = np.array([neuron(input_activations) for neuron in self.hidden_layer1])

        # Pass activations through the second hidden layer
        hidden_activations2 = np.array([neuron(hidden_activations1) for neuron in self.hidden_layer2])

        # Pass activations through the output layer
        output = self.output_layer(hidden_activations2)

        return output

def visualize_network(network):
    fig = go.Figure()

    # Add input layer nodes
    for i in range(3):
        fig.add_trace(go.Scatter(x=[1], y=[i+1], mode='markers', marker=dict(size=20), name=f'Input {i+1}'))

    # Add first hidden layer nodes
    for i in range(4):
        fig.add_trace(go.Scatter(x=[2], y=[i+1], mode='markers', marker=dict(size=20), name=f'Hidden1 {i+1}'))
        for j in range(3):
            fig.add_trace(go.Scatter(x=[1, 2], y=[j+1, i+1], mode='lines', line=dict(color='blue'), showlegend=False))

    # Add second hidden layer nodes
    for i in range(4):
        fig.add_trace(go.Scatter(x=[3], y=[i+1], mode='markers', marker=dict(size=20), name=f'Hidden2 {i+1}'))
        for j in range(4):
            fig.add_trace(go.Scatter(x=[2, 3], y=[j+1, i+1], mode='lines', line=dict(color='blue'), showlegend=False))

    # Add output layer node
    fig.add_trace(go.Scatter(x=[4], y=[1], mode='markers', marker=dict(size=20), name='Output'))
    for i in range(4):
        fig.add_trace(go.Scatter(x=[3, 4], y=[i+1, 1], mode='lines', line=dict(color='blue'), showlegend=False))

    fig.update_layout(title='Neural Network Visualization',
                      xaxis=dict(title='Layers'),
                      yaxis=dict(title='Neurons'),
                      showlegend=True)

    return fig

# Example usage:
network = NeuralNetwork()
inputs = np.array([0.5, 0.3, 0.1])
output = network.forward(inputs)
print("Network output:", output)
fig = visualize_network(network)
fig.show()
