#!/usr/bin/env python
import glob
import os
import pickle
import numpy
from scipy.misc import imsave
from joblib import Parallel, delayed


def mkdir_p(d):
  try:
    os.makedirs(d)
  except OSError as err:
    if err.errno != 17:
      raise


def do_file(fn):
  fns_models = [fn.replace(model1, model) for model in models_in]
  posteriors_models = [pickle.load(open(f, "rb")) for f in fns_models]
  posteriors_stacked = numpy.stack(posteriors_models, axis=0)
  posteriors = numpy.mean(posteriors_stacked, axis=0)
  f_out = fn.replace(model1, model_out)
  print(f_out)
  mkdir_p(os.path.dirname(f_out))
  pickle.dump(posteriors, open(f_out, "wb"), pickle.HIGHEST_PROTOCOL)
  recog = numpy.argmax(posteriors, axis=2)
  imsave(f_out.replace("pickle", "png"), recog)

model1 = "paper_VOC2_noDAVIS_oneshot6_2"
model2 = "iterative_forward_no_underscore"

models_in = [model1, model2]
model_out = "ensemble"

fwd_path = "/home/mahadevan/vision/savitar/forwarded/"

assert not os.path.isdir(fwd_path + model_out), fwd_path + model_out

files = glob.glob(fwd_path + model1 + "/valid/*/*.pickle")
print(fwd_path + model1 + "/valid/*/*.pickle")

#for f in files:
#  do_file(f)
Parallel(n_jobs=20)(delayed(do_file)(f) for f in files)
