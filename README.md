# KoBERT Toxicity Detection

This project implements a toxicity detection model using KoBERT, aimed at classifying toxicity across five categories: gender, age, appearance, individual/group, and cleanness.

## Project Overview

The model is trained on a manually labeled dataset of 4,000 comments. These comments were labeled for five different toxicity categories, based on the dataset from [Korean Hate Speech](https://github.com/kocohub/korean-hate-speech).
This repository contains code and trained models for a multi-label text classification task aimed at detecting various types of toxic or biased language in Korean text. The model predicts the presence of five categories in an input sentence.

## Dataset

- **Labeled Data:** 4,000 manually annotated comments.
- **Categories:**  
  - Gender  
  - Age  
  - Appearance  
  - Individual/Group  
  - Cleanness
- **Source:** [Korean Hate Speech Dataset](https://github.com/kocohub/korean-hate-speech)

The task is framed as a multi-label classification problem where each label can be independently present or absent.
---
## Model Training and Performance

- The model was trained for 35 epochs using a training dataset with batch sizes of 88 (training) and 25 (validation).  
- Training and validation loss steadily decreased, with validation accuracy stabilizing around **76.3%**.  
- The final test set performance:  
  - **Test Loss:** 0.1305  
  - **Test Accuracy:** 75.63%  
  - **Macro F1 Score:** 0.1201  

> **Note:** The low Macro F1 indicates class imbalance or difficulty in detecting certain labels, particularly those that appear less frequently ("gender", "age", "appearance").

---
## Input and Output Format

- **Input:** A Korean text sentence.  
- **Output:**  
  - Raw probabilities for each of the 5 labels (values between 0 and 1).  
  - Binary predictions per label, using a threshold of 0.5.

## Example Usage

```python
input_sentence = "30대 아줌마들;; 고만들 하세요;"
raw_probs, binary_preds = model.predict(input_sentence)

print("Raw Probabilities:", raw_probs)
print("Predicted Labels:")
for idx, label in enumerate(['gender', 'age', 'appearance', 'individual/group', 'cleanness']):
    print(f"  - {label:15}: {'YES' if binary_preds[idx] else 'NO'} (p={raw_probs[idx]:.3f})")
Example Output:
Raw Probabilities: [0.671, 0.967, 0.315, 0.254, 0.092]
Predicted Labels:
  - gender        : YES (p=0.671)
  - age           : YES (p=0.967)
  - appearance    : NO  (p=0.315)
  - individual/group: NO  (p=0.254)
  - cleanness     : NO  (p=0.092)
```
---
Dataset and Preprocessing
- The model was trained on a dataset containing Korean text annotated with multiple labels indicating types of bias or toxicity.
- Input sentences are tokenized and fed into the model in batches (train batch size: 88, validation batch size: 25).
- No additional preprocessing details are included here but may include normalization and tokenization compatible with the underlying model architecture.

Model Architecture and Training Details
- Training utilized a focal loss per label, optimized over 35 epochs.
- The training logs show consistent improvement in training loss and accuracy, with validation accuracy plateauing near 76%.

Limitations and Future Work
- Low Macro F1 Score: The model struggles with some classes, likely due to data imbalance or challenging semantics.
- Thresholding: Using a fixed threshold of 0.5 for all labels might not be optimal. Threshold tuning or using class-specific thresholds could improve results.
- Data Augmentation: Expanding and balancing the training dataset could help with rare classes.
- Multi-Language Support: Currently tailored for Korean text, but architecture could be adapted for other languages.
---
How to Run
1. Clone the repo.
2. Prepare your input dataset or individual sentences.
3. Load the pretrained model weights (if provided).
4. Use the provided inference scripts or API to classify new sentences.
5. Optionally fine-tune the model on your own labeled data.

## Installation

Install required packages (example):

```bash
pip install -r requirements.txt
```
