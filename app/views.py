
# coding: utf-8

# In[1]:
from flask import render_template,flash,redirect, Flask, request, escape
from app import app


@app.route('/')
def index() -> 'html':
    return render_template('index.html', the_title = "喵")
       

# In[ ]:



