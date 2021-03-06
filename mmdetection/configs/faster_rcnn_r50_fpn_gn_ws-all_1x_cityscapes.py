_base_ = 'faster_rcnn_r50_fpn_1x_cityscapes.py'
conv_cfg = dict(type='Conv2d')
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    pretrained='torchvision://resnet50',
    backbone=dict(conv_cfg=conv_cfg, norm_cfg=norm_cfg),
    neck=dict(conv_cfg=conv_cfg, norm_cfg=norm_cfg),
    roi_head=dict(
        bbox_head=dict(
            type='Shared4Conv1FCBBoxHead',
            conv_out_channels=256,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg)))
