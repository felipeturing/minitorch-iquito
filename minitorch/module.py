	## Task 0.4
	## Modules

class Module:
	def __init__(self):
		self._modules = {}
		self._parameters = {}
		self.mode = "train"

	def modules(self):
		return self.__dict__["_modules"].values()

	def train(self):
		self.mode = "train"
		for child_module in self.modules():
			child_module.mode = "train"

	def eval(self):
		self.mode = "eval"
		for child_module in self.modules():
			child_module.mode = "eval"

	def named_parameters(self):
		d = {}
		for key, value in self._parameters.items():
			d[key] = value

		for module_name, module_class in self._modules.items():
			for key, value in module_class._parameters.items():
				key = str(module_name) + '.' + key
				d[key] = value
		return d

	def parameters(self):
		return self.named_parameters().values()

	def add_parameter(self, k, v):
		val = Parameter(v)
		self.__dict__["_parameters"][k] = val
		return val

	def __setattr__(self, key, val):
		if isinstance(val, Parameter):
			self.__dict__["_parameters"][key] = val
		elif isinstance(val, Module):
			self.__dict__["_modules"][key] = val
		else:
			super().__setattr__(key, val)

	def __getattr__(self, key):
		if key in self.__dict__["_parameters"]:
			return self.__dict__["_parameters"][key]

		if key in self.__dict__["_modules"]:
			return self.__dict__["_modules"][key]

		return self.__getattribute__(key)

	def __call__(self, *args, **kwargs):
		return self.forward(*args, **kwargs)

	def forward(self):
		assert False, "Not Implemented"

	def __repr__(self):
		def _addindent(s_, numSpaces):
			s = s_.split("\n")
			if len(s) == 1:
				return s_
			first = s.pop(0)
			s = [(numSpaces * " ") + line for line in s]
			s = "\n".join(s)
			s = first + "\n" + s
			return s

		child_lines = []

		for key, module in self._modules.items():
			mod_str = repr(module)
			mod_str = _addindent(mod_str, 2)
			child_lines.append("(" + key + "): " + mod_str)
		lines = child_lines

		main_str = self.__class__.__name__ + "("
		if lines:
			# simple one-liner info, which most builtin Modules will use
			main_str += "\n  " + "\n  ".join(lines) + "\n"

		main_str += ")"
		return main_str


class Parameter:
	def __init__(self, x=None):
		self.value = x
		if hasattr(x, "requires_grad_"):
			self.value.requires_grad_(True)

	def update(self, x):
		self.value = x
		if hasattr(x, "requires_grad_"):
			self.value.requires_grad_(True)

	def __repr__(self):
		return repr(self.value)


class Module1(Module):
	def __init__(self):
		super().__init__()
		self.module_a = Module2(5)
		self.module_b = Module2(3)
		self.parameter_a = Parameter(40)

class Module2(Module):
	def __init__(self, extra=0):
		super().__init__()
		self.parameter_a = Parameter(50)
		self.parameter_b = Parameter(100)
		self.non_parameter = 10
		for i in range(extra):
			self.add_parameter(f"extra_parameter_{i}", None)

#Pruebas del archivo
# ~ module1 = Module1()
# ~ module2 = Module2(2)
# ~ module1.eval()
# ~ print(module1.mode)
# ~ for child in module1.modules():
	# ~ print(child.mode)
# ~ print(len(module2.modules()))
# ~ print(module2.named_parameters())
# ~ print(module1.__dict__["_modules"].keys())
# ~ print(module1.named_parameters())
# ~ def recursive_params():
	# ~ if
	# ~ dic = module1.__dict__["_parameters"]
# ~ for child in module1.modules():
	# ~ print(child)
# ~ print(dic)
