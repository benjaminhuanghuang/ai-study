Let's take an example of an RNN that takes as input the last four words in a sequence and predicts the next word.


## The vanishing gradients problem


## The gated recurrent unit(GRU)
Has 1 gates
A GRU computes an additional update gate at each time step. 
The update gate produces a result of zero or one. 
If the value is zero, then the current input is ignored and the previous hidden state becomes the current hidden state.

## Long short-term memory
• Regular RNN pass on the previous hidden states to the next time step, with incremental delay
• LSTM uses multiple gates to decide if the previous hidden state needs to be passed on or ignored
• Ensure long term memory for certain features
• LSTM is better for longer sequences, GRU is more efficient

Has 3 gates

## Bidirectional RNNs
• A time step in a sequence may be dependent upon both
What occurred in the previous time steps
What occurred in the future time 

• Use Cases
    Named Entity Recognition
    Speech Recognition
    Grammar Checker
