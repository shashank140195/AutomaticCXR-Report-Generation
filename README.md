Shashank Gupta, Yuhang Jiang, Abdullah-Al-Zubaer Imran
shashank.gupta@uky.edu, yuhang.jiang@uky.edu, aimran@uky.edu


Project Title : Automated Medical Report Generation from Chest X-Rays Images


Problem Statement: The current manual process of generating medical reports from chest X-ray images is time-consuming, prone to errors and reduces overall efficiency in the healthcare system. The manual effort takes away valuable time and resources from other important tasks, which slows down the diagnostic process, especially in emergency situations. There is a clear need for a solution that addresses these issues, and automation provides that solution. Automating the medical report generation process has several key benefits, including improved accuracy and efficiency, a more comprehensive and relevant summary, enhanced clinical decision-making, improved patient care, scalability, and cost savings. Automated report generation can handle a large volume of images and reports, reducing the burden on healthcare professionals and freeing up resources for other important tasks. In conclusion, the implementation of an automated solution in medical report generation has the potential to revolutionize the healthcare industry, providing healthcare professionals with the tools they need to provide better patient care.


Methodological Plan (dataset, code, potential model/architecture, etc.): In this project, we adopt the MIMIC-CXR dataset which contains chest x-ray images and associated radiology reports[1]. We propose to develop a model tool for generating radiology reports with a given chest x-ray image. Our proposed model consists of two components: an image-encoder for extracting features from images, and a decoder for generating textual reports. The image-encoder component has the potential to be implemented using either a Convolutional Neural Network (CNN) based or a Vision Transformer[2] architecture. The decoder component, on the other hand, can be implemented using either a Transformer-based or a Long Short-Term Memory (LSTM)[3] based architecture. We are aiming to extract image features from above mentioned encoder and feeding output of encoder to decoder to extract information and generate output sequence. Our work will be built upon HuggingFace library, a Python library that provides access to a large collection of pre-trained Natural language Processing and Computer Vision models through a simple and consistent interface with the PyTorch framework. We will be training on MIMIC CXR dataset and will also validate on IU-Xray dataset[4] and use BLEU score for evaluation and results. 

Potential clinical impact (upon successful completion, how it could impact clinically): The successful implementation of an automated medical report generation system has the potential to bring about significant improvements, including increased accuracy, quicker diagnoses, prompt results for patients and cost savings. These advancements can completely transform the healthcare industry and result in better patient outcomes.
