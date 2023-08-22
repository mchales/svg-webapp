# svg-webapp

In this project my team explored using different types of ML models for for transforming images (png) to scalable vector graphics (SVG). We looked at Pix2Code, generative models, and image captioning models. This repository includes my focus on the image captioning model trained on a custom SVG dataset.  

![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXVwN3BwbDN3bzFsYm5ldHltbXNndXVlZW51MDdwdmlodGxjaG8zeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/54m1lugHdq25pa0nki/giphy.gif)

In this gif you can see me feeding the model an unseen png image and the models output (SVG code) rendered in an SVG viewer. 

To start, run the command
```
python app.py
```

In the test-images folder there are pngs that the model has not seen.

Note in requirments.txt I change tensorflow-macos to tensorflow-cpu for compatability with Heroku. 

There are some unrelated files for deployment on Heroku.

To train your own model, add png images into images folder (https://drive.google.com/file/d/1LqB-qagurRoPD6CmVfC0c707hcW6BvW5/view?usp=sharing) and follow the code in svg-captioning.ipynb. You can change the output path of your model to not overwrite the existing.
