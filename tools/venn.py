from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt

omega = set(['10', '11', '01', '00'])
A=set(['10', '11'])
B=set(['11', '01'])

def plot_venn(highlights):
    """ Plot a venn diagram with two intersecting sets A and B
    and highlight any combination of A, B and omega. """
    to_hide = set(['10', '11', '01'])-set(highlights)
    figure = plt.figure()
    ax=plt.gca()
    ax.text(0.7, 0.5, '$\Omega$', fontsize=16)
    if '00' in highlights:
        figure.patch.set_facecolor('grey')
    subsets={'10': 1, '01': 1, '11': 1}
    v = venn2(subsets, set_labels = ('A', 'B'), alpha=1)
    for p in to_hide:
        v.get_patch_by_id(p).set_color('w')
        v.get_patch_by_id(p).set_alpha(1)
    for p in {'10', '11', '01'}:
        v.get_label_by_id(p).set_text('')
    venn2_circles(subsets)
    plt.show()