python export_inference_graph.py  \
        --input_type image_tensor  \
        --pipeline_config_path pipeline.config  \
        --trained_checkpoint_prefix models/model/train/model.ckpt-28000  \
        --output_directory data/ssd_hand_inference_graph
