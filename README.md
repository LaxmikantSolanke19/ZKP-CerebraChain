\# ZKP-CerebraChain



\### Privacy-Preserving Federated Brain Tumor Detection using Zero-Knowledge Proofs



ZKP-CerebraChain is a prototype for \*\*privacy-preserving and verifiable AI-based brain tumor detection\*\*. It combines MRI image classification with \*\*Zero-Knowledge Proofs (ZKP)\*\* to demonstrate how an AI prediction can be cryptographically verified without exposing the underlying private computation.



\---



\## Overview



Hospitals possess sensitive MRI data that cannot be freely shared. ZKP-CerebraChain explores a privacy-preserving approach where:



\* MRI data remains local.

\* AI inference is performed locally.

\* The prediction can be represented as a private value.

\* A Zero-Knowledge Proof verifies that the claimed prediction satisfies the required condition.

\* The proof can be verified independently.



This project is currently implemented as a \*\*working prototype\*\* demonstrating the AI inference and ZKP verification pipeline.



\---



\## Key Features



\* Brain MRI image classification

\* Local AI model inference

\* 240 × 240 grayscale MRI input

\* Binary tumor / no-tumor prediction

\* Zero-Knowledge circuit using Circom

\* Groth16 proof system

\* BN128 elliptic curve

\* Witness generation and verification

\* Cryptographic proof generation

\* Independent proof verification



\---



\## AI Model



The project uses a \*\*Sequential CNN model built with TensorFlow/Keras\*\*.



| Property          | Value                 |

| ----------------- | --------------------- |

| Framework         | TensorFlow / Keras    |

| Architecture      | Sequential CNN        |

| Input Shape       | 240 × 240 × 1         |

| Output Shape      | 1                     |

| Parameters        | 12,937,985            |

| Output Activation | Sigmoid               |

| Task              | Binary Classification |



\### Model Architecture



```text

Input: 240 × 240 × 1

&#x20;       ↓

Conv2D (32 filters)

&#x20;       ↓

MaxPooling2D

&#x20;       ↓

Conv2D (64 filters)

&#x20;       ↓

MaxPooling2D

&#x20;       ↓

Conv2D (128 filters)

&#x20;       ↓

MaxPooling2D

&#x20;       ↓

Flatten

&#x20;       ↓

Dense (128)

&#x20;       ↓

Dropout (0.5)

&#x20;       ↓

Dense (1, Sigmoid)

```



\---



\## MRI Inference



The model accepts a grayscale MRI image and resizes it to:



```text

240 × 240 × 1

```



The model produces a probability between `0` and `1`.



Example:



```text

Prediction: 0.980742

Class: TUMOR

```



A value closer to `1` indicates the model predicts tumor, while a value closer to `0` indicates no tumor.



\---



\## Zero-Knowledge Proof



The project uses \*\*Circom + snarkJS + Groth16\*\* for the ZKP pipeline.



The current circuit verifies the relationship between:



```text

prediction

expected value

```



The circuit produces:



```text

valid = prediction - expected

```



When the prediction and expected value satisfy the circuit condition, the witness is valid and a Groth16 proof can be generated and verified.



\### ZKP Pipeline



```text

AI Prediction

&#x20;     ↓

Private Prediction

&#x20;     ↓

Expected Value

&#x20;     ↓

Circom Circuit

&#x20;     ↓

Witness Generation

&#x20;     ↓

Groth16 Proof

&#x20;     ↓

Proof Verification

&#x20;     ↓

VALID

```



\---



\## ZKP Verification Status



The following steps have been successfully tested:



```text

Circom Circuit Compilation      ✅

R1CS Generation                 ✅

WASM Generation                ✅

Powers of Tau                  ✅

Groth16 Setup                   ✅

ZKey Contribution               ✅

Verification Key                ✅

Witness Generation              ✅

Witness Checking                ✅

Proof Generation                ✅

Proof Verification              ✅

```



Example verification result:



```text

\[INFO] snarkJS: OK!

```



\---



\## Project Structure



```text

ZKP-CerebraChain/

│

├── model/

│   ├── config.json

│   └── metadata.json

│

├── scripts/

│   ├── test\_mri.py

│   └── verify\_model.py

│

├── zk/

│   ├── model\_update.circom

│   ├── model\_update.r1cs

│   ├── model\_update.sym

│   └── verification\_key.json

│

├── test\_tumor.jpg

├── .gitignore

└── README.md

```



\---



\## Technologies Used



\### AI / Machine Learning



\* Python

\* TensorFlow

\* Keras

\* NumPy

\* Pillow



\### Zero-Knowledge Proof



\* Circom 2.2.3

\* snarkJS 0.7.6

\* Groth16

\* BN128



\### Development



\* VS Code

\* Git

\* GitHub



\---



\## Current Prototype Workflow



```text

MRI Image

&#x20;   ↓

Preprocessing

&#x20;   ↓

CNN Model

&#x20;   ↓

Tumor Prediction

&#x20;   ↓

ZKP Input

&#x20;   ↓

Witness

&#x20;   ↓

Groth16 Proof

&#x20;   ↓

Verification

```



\---



\## Example



For a sample tumor MRI:



```text

Input:

test\_tumor.jpg



Model Prediction:

0.9807420372962952



Prediction Class:

TUMOR

```



The prediction can then be used in the ZKP demonstration to generate and verify a cryptographic proof.



\---



\## Privacy Concept



The long-term goal of ZKP-CerebraChain is to support a federated healthcare environment where hospitals can collaboratively improve AI models without directly sharing sensitive patient MRI data.



```text

Hospital A ──┐

&#x20;            │

Hospital B ──┼── Federated AI Collaboration

&#x20;            │

Hospital C ──┘

&#x20;                   ↓

&#x20;            Model Updates

&#x20;                   ↓

&#x20;            ZKP Verification

&#x20;                   ↓

&#x20;         Verified Collaboration

```



\---



\## Current Limitations



This repository contains a \*\*prototype implementation\*\*.



The current ZKP circuit demonstrates verification of the prediction relationship. It does not yet prove the complete CNN inference computation inside the zero-knowledge circuit.



Future versions can extend the system toward:



\* Federated learning

\* Multiple hospital nodes

\* Secure model-update verification

\* On-chain proof verification

\* IPFS-based commitments

\* Smart contract integration

\* Privacy-preserving aggregation

\* Full verifiable AI inference



\---



\## Disclaimer



This project is an experimental prototype for research, demonstration, and hackathon purposes. It is \*\*not a certified medical diagnostic system\*\* and should not be used for clinical diagnosis.



\---



\## Project Status



\*\*Prototype Status: Working\*\*



AI Model Verification: ✅

MRI Inference: ✅

ZKP Circuit: ✅

Witness Generation: ✅

Groth16 Proof: ✅

Proof Verification: ✅



\---



\## Author



\*\*ZKP-CerebraChain Team\*\*



Built as a prototype for privacy-preserving and verifiable healthcare AI.



