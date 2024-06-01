import numpy as np
import torch
import sys
import os


'''
    print variables' shape in locals()
    usage: vars = locals().copy()
           print_var_shapes(vars)
'''
def print_var_shapes(locals):
        for name, var in locals.items():
            if hasattr(var, 'shape'):
                print(f"{name}: {var.shape}")
