# cs175-project
You may checkout the project report [here](https://i.cs.hku.hk/~hylei/FinalReport.pdf) to get a better understanding of the results.

Pipeline Overview:
1.	Data Cleaning and Generate TFRecord Files
2.	Model Training and Testing (at run time)
3.	Export model for inference

Data Cleaning and Generate TFRecord Files
Data Cleaning
-	Open data_cleaning.ipynb
-	The notebook consists of two parts: part 1 is to generate training and test folders, part 2 is about building csv files for training and test images based on annotation data.
-	Part 1:
o	Configure input and output file paths, i.e.,
	`source`: source folder path of image files
	`train_dst`: destination folder where you want to put sampled training images
	`test_dst`: destination folder where you want to put sampled test images
	`annotation_dst`: the path to the file in which you put labelled data
-	Part 2:
o	In function generate_label_file:
	`img_dir` is the directory in which you put your training or test images
	`label_dst` is a name given to the generated csv file
	`annotation_data` is a json object
	By default, csv files are saved under data/ directory under the same folder as data_cleaning.ipynb (i.e., current folder)
o	To summarize, this function will generate a csv file and save it under folder "data/", with a name you pass to it.
-	Click `Cell`, and then `Run All`.
-	Done!

Convert to TFRecord
-	There are three files related to this operation:
o	generate_train_tfrecord.py
o	generate_test_tfrecord.py
o	generate_tfrecord.sh
-	Python files are the same except for their paths to images.  They have the following flags:
o	`csv_input`: the path to a csv file from which you want to generate the TFRecord file
o	`output_path`: the path you want to save TFRecord
-	generate_tfrecord.sh runs python files with the following flags:
o	--csv_input = data/train.csv --output_path = data/train.record
o	--csv_input = data/test.csv --output_path = data/test.record
-	Run ./generate_tfrecord.sh, and then you can check data/ folder to see if record files are in it.

Model Training and Testing
I downloaded pre-trained `ssd_mobilenet_v2_coco_2018_03_29` model from TensorFlow model zoo, and the TFRecords generated above are in a structure conforming to this model.

There are basically two steps:
-	Modify pipeline.config (configure training settings), which is initially in the downloaded model;
-	Configure other settings, mostly file paths.

Note that a label_map.pbtxt should be added to data/ directory, it specifies what kind of classes the detector is supposed to identify.  In our model there is only one class, which is hand.

label_map.pbtxt:

item {
id: 1
name: 'hand'
}

Modify config file
The config file consists of 5 parts:
1.	The model configuration.  This defines what type of model will be trained (i.e., meta-architecture, feature extractor)
2.	The train_config, which decides what parameters should be used to train model parameters (i.e., SGD parameters, input preprocessing and feature extractor initialization values)
3.	The eval_config, which determines what set of metrics will be reported for evaluation (PASCAL VOC metrics)
4.	The train_input_config, which defines what dataset the model should be trained on
5.	The eval_input_config, which defines what dataset the model will be evaluated on.  Typically, this should be different from the training input dataset.
A more detailed instruction is available on https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md

Training
`train.py` has the following flags
-	`train_dir`: path to train directory
-	`pipeline_config_path`: path to pipeline configuration file

`run_train.sh` basically runs` train.py` with
-	--train_dir = models/model/train
-	--pipeline_config_path=pipeline.config (in the same directory as train.py)

Run Training script with
-	./run_train.sh

Monitor Training Progress Using TensorBoard
-	Run the command in terminal:
o	tensorboard –logdir=models/model (path to model directory)

Testing is the same.  More details about training and evaluation can be seen here.

Exporting Inference Graph and Visualize
Two files involved:
-	`export_inference_graph.py`
-	`export_graph.sh`

After training, the new model checkpoints are saved under `models/model/train` directory.  `export_inference_graph.py` generates a frozen map using those model checkpoints.   It has the following flags:
-	`input_type`: specifies the type of input, in our case it is image_tensor
-	`pipeline_config_path`: path to config file
-	`trained_checkpoint_prefix`: in our case, it is models/model/train/model.ckpt
-	`output_directory`: path to exported model directory, I set it to data/ssd_hand_inference_graph

Run ./export_graph.sh.  Then open file object_detection_tutorial.ipynb.  I’ve changed it a bit so that you can visualize model output by running all the way down to the end.  

Details can be seen here: https://pythonprogramming.net/testing-custom-object-detector-tensorflow-object-detection-api-tutorial/.
