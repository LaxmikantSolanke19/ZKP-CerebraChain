pragma circom 2.2.3;

template ModelUpdate() {

    signal input prediction;
    signal input expected;
    signal output valid;

    // Prove that the private prediction
    // matches the committed expected value.
    valid <== prediction - expected;

}

component main = ModelUpdate();