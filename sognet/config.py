from detectron2.config import CfgNode as CN


def add_sognet_config(cfg):
    """
    Add configs for SOGNet
    """
    _C = cfg

    _C.MODEL.SEM_SEG_HEAD.NUM_LAYERS = 3

    _C.MODEL.SOGNET = CN()
    _C.MODEL.SOGNET.INSTANCE_LOSS_WEIGHT = 1.0

    _C.MODEL.SOGNET.COMBINE = CN({"ENABLED": True})
    _C.MODEL.SOGNET.COMBINE.OVERLAP_THRESH = 0.5
    _C.MODEL.SOGNET.COMBINE.STUFF_AREA_LIMIT = 4096
    _C.MODEL.SOGNET.COMBINE.INSTANCES_CONFIDENCE_THRESH = 0.5

    _C.MODEL.SOGNET.RELATION = CN({"ENABLED": True})
    _C.MODEL.SOGNET.RELATION.CLS_EMBEDDING_DIM = 128
    _C.MODEL.SOGNET.RELATION.POS_EMBEDDING_DIM = 128
    _C.MODEL.SOGNET.RELATION.LOSS_WEIGHT = 1.0

    _C.MODEL.SOGNET.PANOPTIC = CN()
    _C.MODEL.SOGNET.PANOPTIC.IGNORE_INDEX = 255
    _C.MODEL.SOGNET.PANOPTIC.LOSS_WEIGHT = 1.0
