# n-terminus-branch-points

## Overview:

This repository houses the codebase for a research project done in collaboration with Dr. Sarah Denha of Oakland University, focused on automating the identification and counting of dendritic branch points in fruit fly (Drosophila) brains, specifically targeting Spinocerebellar Ataxia type 5 (SCA5) pathology.

Preview of the model's performance on test image (model identified branch points are annotated with tiny white octagons):

![20x-Delta-N-GM-120HR-L1-N1-A3-FINAL-SAD111919](https://github.com/aryandhr/n-terminus-branch-points/assets/122699104/124d9b45-824a-40fc-be2b-054f002916a8)

## Project Highlights:

- **Research Context:** Collaborative work with PhD candidate Sarah Denha of Oakland University on neurodegenerative disorders, particularly SCA5.
  
- **Objective:** Develop an automated system for identifying and counting dendritic branch points in fruit fly brains using machine learning and computer vision techniques.

- **Current Status:** The object detection model currently detects about 18% of branch points.

- **Dataset Challenges:** The dataset comprises 28 images with incomplete labeling. Strategies are being explored, such as dividing images into smaller sections or using white squares to augment the dataset.

## Project Structure:

- **`model.ipynb`**: Contains the source code for the object detection model and any related scripts.
- **`predictions`**: Contains unseen images by the model and it's predictions on them.

## Future Enhancements:

- **Augment Dataset:** Implement chosen strategy (e.g., dividing images, white squares) to improve model accuracy with limited labeled data.

- **Model Optimization:** Explore techniques to enhance the accuracy of the object detection model.

- **Collaboration Opportunities:** Discuss potential collaborations with neuroscience and genetics communities for feedback and improvement.

## Acknowledgments:

- A huge thank you to Sarah Denha for the opportunity to collaborate on this project.

## License:

- Protected under the Apache 2.0 License

## Contact:

- dhararya@msu.edu for inquiries or collaboration opportunities.
