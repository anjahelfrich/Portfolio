import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(15,15), subplot_kw=dict(projection="polar"))
fig.tight_layout()

#Inputs
skills={'Programming':
            {'Python': [50,
                        {'arcpy':10,
                         'geo/pandas':10,
                         'numpy':10,
                         'os':10,
                         'time':10,
                         'gdal':10,
                         'matplotlib':10,
                         'scipy':10,
                         'tensorflow':10,
                         'django':10}],
            'SQL':30,
            'HTML/CSS':10,
            'Javascript':5,
            'C++':5},
        'GIS':
            {'Esri': [70,
                      {'ArcGIS Desktop': 50,
                       'ArcGIS Pro': 30,
                       'ArcGIS Online': 20}],
            'QGIS': 15,
            'Remote Sensing': [15,
                               {'ENVI': 60,
                                'ERDAS': 40}]},
        'Project Management':
            {'Leadership':20,
             'Remote':20,
             'Agile':20,
             'Communication':20,
             'Documentation':20}}

# Inner
main_bins = 1 / 3
inner_values = np.array([main_bins, main_bins, main_bins])
inner_radians = inner_values * 360 * (np.pi / 180)
inner_labels = skills.keys()

mid_width, out_width, mid_labels, out_labels = [], [], [], []

# Inner
for key, value in skills.items():
    print(key)
    # Middle
    for k, v in value.items():
        print(k)
        mid_labels.append(k)
        if type(v) == list:
            mid = v[0] * 3.6 * (np.pi / 180) * main_bins
            mid_width.append(mid)
            # Outer
            for x, y in v[1].items():
                print(x)
                out_labels.append(x)
                out = mid * (y / 100)
                out_width.append(out)
        else:
            out_labels.append('')
            mid = v * 3.6 * (np.pi / 180) * main_bins
            mid_width.append(mid)
            out_width.append(mid)

# Shift Positions to start at 0
inner_positions = np.cumsum(inner_radians)
inner_positions = np.append(0, inner_positions)
inner_positions = np.delete(inner_positions, -1)

mid_positions = np.cumsum(mid_width)
mid_positions = np.append(0, mid_positions)
mid_positions = np.delete(mid_positions, -1)

out_positions = np.cumsum(out_width)
out_positions = np.append(0, out_positions)
out_positions = np.delete(out_positions, -1)

# Colors
inner_colors = ['#233647', '#448D76', '#792A32']

mid_colors = ['#1D3557', '#274769', '#31587A', '#3B6A8C', '#457B9D',  # Code
              '#427B2E', '#568F4B', '#6AA267',   # GIS
              '#904653', '#884556', '#7F4458', '#76435A', '#6D415C']  # PM

outer_colors = ['#13414F','#154857','#1B5C64','#28667E','#4C7586','#3A7C8D','#278293','#2C95B5','#51A9C3','#75BCD1', # Python
                '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF',  # Programming Blanks
                '#8A862C', '#AE8C2B', '#D29129',  # Esri
                '#FFFFFF',  # GIS Blank
                '#AAA153', '#9CA660',  # Remote Sensing
                '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']  # Project Management blanks

# Outer heights
outer_heights = [1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2,  # Python
                 0, 0, 0, 0,  # Programming Blanks
                 1, 0.8, 0.5,  # Esri
                 0,  # GIS Blank
                 0.5, 0.5,  # Remote Sensing
                 0, 0, 0, 0, 0]  # Project Management blanks

# Plot bars
ax.bar(x=out_positions,
       width=out_width, bottom=1.6, height=outer_heights, color=outer_colors, edgecolor='w', linewidth=1, align="edge")

ax.bar(x=mid_positions,
       width=mid_width, bottom=0.8, height=0.8, color=mid_colors, edgecolor='w', linewidth=1, align="edge")

ax.bar(x=inner_positions,
       width=inner_radians, bottom=0.3, height=0.5, color=inner_colors, edgecolor='w', linewidth=1, align="edge")

# Add labels
for x, w, label in zip(inner_positions, inner_radians, inner_labels):
    x = x + (w / 2)
    ax.text(x, 0.15, label, color='white', fontsize='small', fontweight='demi', transform=ax.get_xaxis_transform(),
            rotation_mode="anchor", ha='center', ma='center', va='center')

for x, w, label in zip(mid_positions, mid_width, mid_labels):
    x = x + (w / 2)
    ax.text(x, 0.4, label, color='white', fontsize='small', fontweight='demi', transform=ax.get_xaxis_transform(),
            rotation_mode="anchor", ha='center', ma='center', va='center')

for x, w, h, label in zip(out_positions, out_width, outer_heights, out_labels):
    x = x + (w / 2)
    h = (h/4) + 0.5
    ax.text(x, h, label, color='white', fontsize='small', fontweight='demi', transform=ax.get_xaxis_transform(),
            rotation_mode="anchor", ha='center', ma='center', va='center')

#ax.set(title="A multi-layer pie chart (polar bar chart) created using matplotlib")
ax.set_axis_off()
plt.show()
fig.savefig('skill_pie.png', dpi=300, transparent=True)
