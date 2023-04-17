# svg-webapp

To run, run the command

```
python app.py
```

In the test-images folder there are pngs that the model has not seen.

Note in requirments.txt I change tensorflow-macos to tensorflow-cpu for compatability with Heroku. 

There are some unrelated files for attempting to deploy on Heroku.


To train your own model, add png images into images folder (https://drive.google.com/file/d/1LqB-qagurRoPD6CmVfC0c707hcW6BvW5/view?usp=sharing) and follow the code in svg-captioning.ipynb. You can change the output path of your model to not overwrite the existing.
