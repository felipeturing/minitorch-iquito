# ~ import visdom
# ~ import matplotlib.pyplot as plt
# ~ vis = visdom.Visdom()

# ~ # Loss goes down!
# ~ plt.plot([2.0, 1.0, 0.0], c="blue")
# ~ plt.title("Model Loss")

# ~ # Send to visdom
# ~ vis.matplot(plt, win="loss")

# ~ import matplotlib.pyplot as plt
# ~ vis = visdom.Visdom()

# ~ # Loss goes down!
# ~ plt.plot([2.0, 1.0, 0.0], c="blue")
# ~ plt.title("Model Loss")

# ~ # Send to visdom
# ~ vis.matplot(plt, win="loss")


from project.datasets import Simple, Split, Xor

def classify_Simple(pt):
	if pt[0] < 0.5:
		return 1
	else: 
		return 0

def classify_Split(pt):
	if pt[0] < 0.2 or pt[0] > 0.8:
		return 1
	else: 
		return 0

N = 100
#Simple(N, vis=True).graph("initial", model=classify_Simple)
Split(N, vis=True).graph("initial", model=classify_Split)
