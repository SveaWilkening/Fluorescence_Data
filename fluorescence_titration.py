# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:08:56 2020

@author: svea_
"""

import prntitration as pt

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
palette = ["#4A456A", "#6B8CA6", "#345C64", "#806B5C", "#CAA87D", "#B56470", 
           "#84BB94", "#67504C", "#E98D2B"]
sns.set_palette(palette)
sns.set_style("ticks", {"axes.facecolor": "aliceblue"})
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

location = path_to_file

df_1 = pt.generate_df(location[0])
df_2 = pt.generate_df(location[1])

frexs, frexl = pt.separate_long_short(df_1)
nadhs, nadhl = pt.separate_long_short(df_2)

frexs = pt.separate_x_y(frexs)
frexl = pt.separate_x_y(frexl)
nadhs = pt.separate_x_y(nadhs)

frexs = pt.rename_cols(frexs)
frexl = pt.rename_cols(frexl)
nadhs = pt.rename_cols(nadhs)

# for clearness just plot a sample of the data
long_keep = ["x", "0", "2", "4", "6", "10", "25", "50", "100", "200"]

frexl = frexl[long_keep]

short_keep_1 = ["x", "0", "1", "2", "3", "4", "5", "10"]
short_keep_2 = ["x", "0", "10", "25", "50", "75",  "100", "200"]

frexs_1 = frexs[short_keep_1]
frexs_2 = frexs[short_keep_2]

NADH_keep = ["x", "0", "10", "25", "50", "75",  "125", "200"]

nadhs = nadhs[NADH_keep]

#scaling plots in y-axis
frexs_1 = pt.scale_y_axis(frexs_1, short_keep_1[1:])
frexs_2 = pt.scale_y_axis(frexs_2, short_keep_2[1:])
frexl = pt.scale_y_axis(frexl, long_keep[1:])
nadhs = pt.scale_y_axis(nadhs, NADH_keep[1:])

fig, axes = plt.subplots(2, 2, figsize=(9,7), dpi=400)

#set legend params for these subplots

new_title = '[NADH] in \u03BCM'

ax1 = frexs_1.plot(x="x", ax=axes[0,0], yticks=(np.arange(0,6,1)))
ax2 = frexl.plot(x="x", ax=axes[0,1], yticks=(np.arange(0,17,4)))
ax3 = frexs_2.plot(x="x", ax=axes[1,0], yticks=(np.arange(0,17,4)))
ax4 = nadhs.plot(x="x", ax=axes[1,1], yticks=(np.arange(0,17,4)))

ax1.set_xlabel("")
ax2.set_xlabel("")
ax3.set_xlabel("")
ax4.set_xlabel("")

ax1.set_title("A", loc='left', fontweight='bold')
ax2.set_title("B", loc='left', fontweight='bold')
ax3.set_title("C", loc='left', fontweight='bold')
ax4.set_title("D", loc='left', fontweight='bold')


ax1.legend(title=new_title, title_fontsize=12, labelspacing=0.1, fontsize=10, 
           frameon=False)
ax2.legend(title=new_title, title_fontsize=12, labelspacing=0.05, fontsize=10,
           frameon=False)
ax3.legend(title=new_title, title_fontsize=12, labelspacing=0.1, fontsize=10,
           frameon=False)
ax4.legend(title=new_title, title_fontsize=12, labelspacing=0.1, fontsize=10,
           frameon=False)


fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Fluorescence Intensity (a.u.)")

plt.tight_layout()
plt.show()
