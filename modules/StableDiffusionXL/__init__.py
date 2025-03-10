from utils.hf_utils import list_local_models
from utils.torch_utils import device_list, default_device, str_to_dtype

MODULE_MAP = {
    'SDXLPipelineLoader': {
        'label': 'SDXL Pipeline Loader',
        'description': 'Load the SDXL Pipeline',
        'category': 'loaders',
        'params': {
            'unet_out': {
                'label': 'UNet',
                'type': 'UNet2DConditionModel',
                'display': 'output',
            },
            'text_encoders_out': {
                'label': 'Text Encoders',
                'type': 'SDXLTextEncoders',
                'display': 'output',
            },
            'vae_out': {
                'label': 'VAE',
                'type': 'VAE',
                'display': 'output',
            },
            'pipeline': {
                'label': 'SDXL Pipeline',
                'type': 'pipeline',
                'display': 'output',
            },
            'model_id': {
                'label': 'Model ID',
                'type': 'string',
                'options': list_local_models(filters={"_class_name": r"XLPipeline$"}),
                'display': 'autocomplete',
                'no_validation': True,
                'default': 'stabilityai/stable-diffusion-xl-base-1.0',
            },
            'dtype': {
                'label': 'dtype',
                'options': ['auto', 'float32', 'bfloat16','float16'],
                'default': 'bfloat16',
                'postProcess': str_to_dtype,
            },
            'variant': {
                'label': 'Variant',
                'type': 'string',
                'options': ['', 'fp16', 'emaonly'],
                'default': 'fp16',
                'display': 'autocomplete',
                'no_validation': True,
                'postProcess': lambda x, _: x or None,
            },
            'unet': {
                'label': 'UNet',
                'type': 'UNet2DConditionModel',
                'display': 'input',
            },
            'text_encoders': {
                'label': 'Text Encoders',
                'type': 'SDXLTextEncoders',
                'display': 'input',
            },
            'vae': {
                'label': 'VAE',
                'type': 'VAE',
                'display': 'input',
            },
        },
    },

    'SDXLPromptsEncoder': {
        'label': 'SDXL Prompts Encoder',
        'category': 'text-encoders',
        'params': {
            'text_encoders': {
                'label': 'SDXL Encoders | Pipeline',
                'display': 'input',
                'type': ['pipeline', 'SDXLTextEncoders'],
            },
            'embeds': {
                'label': 'Embeddings',
                'display': 'output',
                'type': 'SDXLEmbeddings',
            },
            'prompt': {
                'label': 'Prompt',
                'type': 'string',
                'display': 'textarea',
            },
            'negative_prompt': {
                'label': 'Negative Prompt',
                'type': 'string',
                'display': 'textarea',
            },
            'prompt_2': {
                'label': 'Prompt CLIP G',
                'type': 'string',
                'display': 'textarea',
                'group': { 'key': 'extra_prompts', 'label': 'Extra Prompts', 'display': 'collapse' },
            },
            'negative_prompt_2': {
                'label': 'Negative Prompt CLIP G',
                'type': 'string',
                'display': 'textarea',
                'group': 'extra_prompts',
            },
            'clip_skip': {
                'label': 'Clip Skip',
                'type': 'int',
                'default': 0,
                'min': 0,
                'max': 10,
            },
            'noise_positive': {
                'label': 'Positive Noise',
                'type': 'float',
                'default': 0.0,
                'display': 'slider',
                'min': 0,
                'max': 1,
                'step': 0.05,
                'group': { 'key': 'noise', 'label': 'Noise', 'display': 'collapse' },
            },
            'noise_negative': {
                'label': 'Negative Noise',
                'type': 'float',
                'default': 0.0,
                'display': 'slider',
                'min': 0,
                'max': 1,
                'step': 0.05,
                'group': 'noise',
            },
            'device': {
                'label': 'Device',
                'type': 'string',
                'options': device_list,
                'default': default_device,
            },
        },
    },

    'SDXLSampler': {
        'label': 'SDXL Sampler',
        'category': 'samplers',
        'style': {
            'maxWidth': '360px',
        },
        'params': {
            'pipeline': {
                'label': 'Pipeline',
                'display': 'input',
                'type': 'pipeline',
            },
            'prompt': {
                'label': 'Embeddings',
                'display': 'input',
                'type': ['SDXLEmbeddings', 'embeddings'],
            },
            'pipeline_out': {
                'label': 'Pipeline',
                'display': 'output',
                'type': 'pipeline',
            },
            'latents': {
                'label': 'Latents',
                'type': 'latent',
                'display': 'output',
            },
            'width': {
                'label': 'Width',
                'type': 'int',
                'display': 'text',
                'default': 1024,
                'min': 8,
                'max': 8192,
                'group': 'dimensions',
            },
            'height': {
                'label': 'Height',
                'type': 'int',
                'display': 'text',
                'default': 1024,
                'min': 8,
                'max': 8192,
                'group': 'dimensions',
            },
            'resolution_picker': {
                'label': 'Resolution',
                'display': 'ui',
                'type': 'dropdownIcon',
                'options': [
                    { 'label': ' 720×1280 (9:16)','value': [720, 1280] },
                    { 'label': ' 768×1344 (0.57)','value': [768, 1344] },
                    { 'label': ' 768×1280 (3:5)', 'value': [768, 1280] },
                    { 'label': ' 832×1152 (3:4)', 'value': [832, 1152] },
                    { 'label': '1024×1024 (1:1)', 'value': [1024, 1024] },
                    { 'label': ' 1152×832 (4:3)', 'value': [1152, 832] },
                    { 'label': ' 1280×768 (5:3)', 'value': [1280, 768] },
                    { 'label': ' 1280×720 (16:9)','value': [1280, 720] },
                    { 'label': ' 1344×768 (1.75)','value': [1344, 768] },
                    { 'label': '---','value': None }, # divider
                    { 'label': ' 512×2048 (0.25)', 'value': [512, 2048] },
                    { 'label': ' 512×1984 (0.26)', 'value': [512, 1984] },
                    { 'label': ' 512×1920 (0.27)', 'value': [512, 1920] },
                    { 'label': ' 512×1856 (0.28)', 'value': [512, 1856] },
                    { 'label': ' 576×1792 (0.32)', 'value': [576, 1792] },
                    { 'label': ' 576×1728 (0.33)', 'value': [576, 1728] },
                    { 'label': ' 576×1664 (0.35)', 'value': [576, 1664] },
                    { 'label': ' 640×1600 (0.4)',  'value': [640, 1600] },
                    { 'label': ' 640×1536 (0.42)', 'value': [640, 1536] },
                    { 'label': ' 704×1472 (0.48)', 'value': [704, 1472] },
                    { 'label': ' 704×1408 (1:2)',  'value': [704, 1408] },
                    { 'label': ' 704×1344 (0.52)', 'value': [704, 1344] },
                    { 'label': ' 832×1216 (0.68)', 'value': [832, 1216] },
                    { 'label': ' 896×1152 (0.78)', 'value': [896, 1152] },
                    { 'label': ' 896×1088 (0.82)', 'value': [896, 1088] },
                    { 'label': ' 960×1088 (0.88)', 'value': [960, 1088] },
                    { 'label': ' 960×1024 (0.94)', 'value': [960, 1024] },
                    { 'label': ' 1024×960 (1.07)', 'value': [1024, 960] },
                    { 'label': ' 1088×960 (1.13)', 'value': [1088, 960] },
                    { 'label': ' 1088×896 (1.21)', 'value': [1088, 896] },
                    { 'label': ' 1152×896 (1.29)', 'value': [1152, 896] },
                    { 'label': ' 1216×832 (1.46)', 'value': [1216, 832] },
                    { 'label': ' 1408×704 (2.0)',  'value': [1408, 704] },
                    { 'label': ' 1472×704 (2.09)', 'value': [1472, 704] },
                    { 'label': ' 1536×640 (2.4)',  'value': [1536, 640] },
                    { 'label': ' 1600×640 (2.5)',  'value': [1600, 640] },
                    { 'label': ' 1664×576 (2.89)', 'value': [1664, 576] },
                    { 'label': ' 1728×576 (3.0)',  'value': [1728, 576] },
                    { 'label': ' 1792×576 (3.11)', 'value': [1792, 576] },
                    { 'label': ' 1856×512 (3.62)', 'value': [1856, 512] },
                    { 'label': ' 1920×512 (3.75)', 'value': [1920, 512] },
                    { 'label': ' 1984×512 (3.88)', 'value': [1984, 512] },
                    { 'label': ' 2048×512 (4.0)',  'value': [2048, 512] },
                ],
                'onChange': { 'action': 'set', 'target': ['width', 'height'] },
                'group': 'dimensions',
            },
            'seed': {
                'label': 'Seed',
                'type': 'int',
                'default': 0,
                'min': 0,
                'display': 'random',
            },
            'steps': {
                'label': 'Steps',
                'type': 'int',
                'default': 25,
                'min': 1,
                'max': 1000,
            },
            'cfg': {
                'label': 'Guidance',
                'type': 'float',
                'default': 7,
                'min': 0,
                'max': 100,
            },
            'num_images': {
                'label': 'Num Images',
                'type': 'int',
                'default': 1,
                'min': 1,
                'max': 1000,
            },
            'scheduler': {
                'label': 'Scheduler',
                'display': 'select',
                'type': ['string', 'scheduler'],
                'options': {
                    'DDIMScheduler': 'DDIM',
                    'DDPMScheduler': 'DDPM',
                    'DEISMultistepScheduler': 'DEIS Multistep',
                    'DPMSolverSinglestepScheduler': 'DPMSolver Singlestep',
                    'DPMSolverMultistepScheduler': 'DPMSolver Multistep',
                    'DPMSolverSDEScheduler': 'DPMSolver SDE',
                    'EulerDiscreteScheduler': 'Euler Discrete',
                    'EulerAncestralDiscreteScheduler': 'Euler Ancestral',
                    'HeunDiscreteScheduler': 'Heun Discrete',
                    'KDPM2DiscreteScheduler': 'KDPM2 Discrete',
                    'KDPM2AncestralDiscreteScheduler': 'KDPM2 Ancestral',
                    'LMSDiscreteScheduler': 'LMS Discrete',
                    'PNDMScheduler': 'PNDM',
                    'UniPCMultistepScheduler': 'UniPC Multistep',
                },
                'default': 'EulerDiscreteScheduler',
            },
            'latents_in': {
                'label': 'Latents | Images',
                'display': 'input',
                'type': ['latent', 'image'],
                #'onChange': { 'action': 'disable', 'target': { 'connected': ['dimensions_group'], 'disconnected': ['strength'] } },
            },
            'sync_latents': {
                'label': 'Sync with previous latents',
                'type': 'boolean',
                'default': False,
                'onChange': { 'action': 'disable', 'target': { True: ['denoise_range', 'steps', 'dimensions_group'], False: [] } },
            },
            'denoise_range': {
                'label': 'Denoise Range',
                'type': 'float',
                'display': 'range',
                'default': [0, 1],
                'min': 0,
                'max': 1,
                'step': 0.01,
            },
            'device': {
                'label': 'Device',
                'type': 'string',
                'options': device_list,
                'default': default_device,
            },
        },
    },

    'SDXLUnetLoader': {
        'label': 'SDXL UNet Loader',
        'description': 'Load the UNet of an SDXL model',
        'category': 'loaders',
        'params': {
            'model': {
                'label': 'UNet',
                'type': 'UNet2DConditionModel',
                'display': 'output',
            },
            'model_id': {
                'label': 'Model ID',
                'type': 'string',
                'options': list_local_models(filters={"_class_name": r"XLPipeline$"}),
                'display': 'autocomplete',
                'no_validation': True,
                'default': 'stabilityai/stable-diffusion-xl-base-1.0',
            },
            'dtype': {
                'label': 'dtype',
                'options': ['auto', 'float32', 'bfloat16','float16'],
                'default': 'bfloat16',
                'postProcess': str_to_dtype,
            },
            'variant': {
                'label': 'Variant',
                'type': 'string',
                'options': ['', 'fp16', 'emaonly'],
                'default': '',
                'display': 'autocomplete',
                'no_validation': True,
            },
        },
    },

    'SDXLTextEncodersLoader': {
        'label': 'SDXL Text Encoders Loader',
        'description': 'Load the CLIP Text Encoders',
        'category': 'loaders',
        'params': {
            'model': {
                'label': 'SDXL Encoders',
                'display': 'output',
                'type': 'SDXLTextEncoders',
            },
            'model_id': {
                'label': 'Model ID',
                'type': 'string',
                'options': list_local_models(filters={"_class_name": r"XLPipeline$"}),
                'display': 'autocomplete',
                'no_validation': True,
                'default': 'stabilityai/stable-diffusion-xl-base-1.0',
            },
            'dtype': {
                'label': 'Dtype',
                'type': 'string',
                'options': ['auto', 'float32', 'float16', 'bfloat16'],
                'default': 'bfloat16',
            },
        },
    },
}



"""
    'SDXLSinglePromptEncoder': {
        'label': 'SDXL Single Prompt Encoder',
        'category': 'text-encoders',
        'params': {
            'text_encoders': {
                'label': 'SDXL Encoders | SDXL Pipeline',
                'display': 'input',
                'type': ['SDXLTextEncoders', 'pipeline'],
            },
            'embeds': {
                'label': 'Embeddings',
                'display': 'output',
                'type': 'SDXLEmbeddings',
            },
            'prompt': {
                'label': 'Prompt',
                'type': 'string',
                'display': 'textarea',
            },
            'prompt_2': {
                'label': 'Prompt CLIP G',
                'type': 'string',
                'display': 'textarea',
                'group': { 'key': 'extra_prompts', 'label': 'Extra Prompts', 'display': 'collapse' },
            },
            'clip_skip': {
                'label': 'Clip Skip',
                'type': 'int',
                'default': 0,
                'min': 0,
                'max': 10,
            },
            'noise': {
                'label': 'Add Noise',
                'type': 'float',
                'default': 0.0,
                'display': 'slider',
                'min': 0,
                'max': 1,
                'step': 0.05,
                'group': { 'key': 'noise', 'label': 'Noise', 'display': 'collapse' },
            },
            'prompt_scale': {
                'label': 'CLIP L',
                'type': 'float',
                'display': 'slider',
                'default': 1.0,
                'min': 0,
                'max': 2,
                'step': 0.05,
                'group': { 'key': 'prompts_scale', 'label': 'Prompts Scale', 'display': 'collapse' },
            },
            'prompt_scale_2': {
                'label': 'CLIP G',
                'type': 'float',
                'default': 1.0,
                'display': 'slider',
                'min': 0,
                'max': 2,
                'step': 0.05,
                'group': 'prompts_scale',
            },
            'device': {
                'label': 'Device',
                'type': 'string',
                'options': device_list,
                'default': default_device,
            },
        },
    },
"""