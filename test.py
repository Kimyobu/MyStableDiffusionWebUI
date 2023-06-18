model = 'Stable Diffusion' #@param ["Lora", "Stable Diffusion"]
model_list = {'Lora': 'Lora', 'Stable Diffusion': 'Stable-diffusion'}
model_path = '/content/drive/MyDrive/stable-diffusion-webui-colab/alohomora/models/' + model_list.get(model)  # type: ignore
print(model_path)