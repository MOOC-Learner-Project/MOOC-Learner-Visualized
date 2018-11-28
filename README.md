# MOOC-Learner-Visualized

Visualize the MOOC learner features with MOOC-Learner-Visualized (MLV)

# Requirements 

<a href="https://www.python.org/" ><img src="https://img.shields.io/badge/Python-blue.svg"></a> <img src="https://img.shields.io/badge/Javascript-blue.svg"> </a><img src="https://img.shields.io/badge/HTML-blue.svg"></a>

<a href="https://www.docker.com/" ><img src="https://img.shields.io/badge/Docker-blue.svg"></a> 
(see [MOOC-Learner-Docker/visualized_base_img](https://github.com/MOOC-Learner-Project/MOOC-Learner-Docker/tree/master/visualized_base_img) )

## Technologies

<a href="http://flask.pocoo.org/" ><img src="https://img.shields.io/badge/Flask-blue.svg"></a>
<a href="https://seaborn.pydata.org/" ><img src="https://img.shields.io/badge/Seaborn-blue.svg"></a>
<a href="https://bokeh.pydata.org/en/latest/" ><img src="https://img.shields.io/badge/Bokeh-blue.svg"></a>
<a href="http://redis.io" ><img src="https://img.shields.io/badge/redis-blue.svg"></a>
<a href="https://www.pandas.pydata.org/" ><img src="https://img.shields.io/badge/Pandas-blue.svg"></a>
<a href="https://www.scipy.org/" ><img src="https://img.shields.io/badge/Scipy-blue.svg"></a>
<a href="https://www.numpy.org/" ><img src="https://img.shields.io/badge/Numpy-blue.svg"></a>

# Installation

See [MOOC-Learner-Docker](https://github.com/MOOC-Learner-Project/MOOC-Learner-Docker/tree/master/README.md)

# Tutorial

Entry point is `autorun.py`. Configuration is done with `config/*yml`, see e.g. `config/sample_config.yml`.

As a backend, run MOOC-Learner-Curated only once, run MOOC-Learner-Quantified only when necessary by command line then
run MOOC-Learner-Visualized (the `Flask` server)

MOOC-Learner-Visualized serves as an interface to visualize  features populated in the `moocdb`. It contains three parts:
- Fetching: which fetches feature columns from feature tables
- Processing: provides several processing functions on data columns, such as filtering, mapping, 
and statistics calculation. Finally, it performs an inner join on relevant feature rows to form a data frame for rendering
- Rendering: provides an interface to configure and render interactive and static plots. The template engine can 
automatically generate html input forms and uses javascript to collect the user input. Adding a new type of plot is as easy 
as adding a new dictionary describing the configuration form and write up a new drawing function, which takes a `pandas` 
dataframe and the all form input as parameters and return a `bokeh` figure instance. Currently we have
 scatter plot, histogram as templates for interactive plots and scatter matrix as the template for static plots. 
 For interactive plots, the user can select or filter a specific feature column with a slider.
