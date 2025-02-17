_base_ = './fpn_van_base_ade20k_40k.py'

# model settings
model = dict(
    pretrained='/path/to/checkpoint',
    backbone=dict(
        type='van_tiny',
        style='pytorch'),
    neck=dict(in_channels=[32, 64, 160, 256]))
