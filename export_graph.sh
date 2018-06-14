python export_inference_graph.py  \
        --input_type image_tensor  \
        --pipeline_config_path pipeline.config  \
        --trained_checkpoint_prefix models/model/train/model.ckpt-120000  \
        --output_directory data/frcnn_hand_inference_graph
