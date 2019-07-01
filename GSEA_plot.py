# libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Make fake dataset
height = [-2.71,-2.60,-2.53,-2.06,-1.51,-1.50,-1.41,1.26,1.34,1.41,1.54,1.55,1.74]

bars = ('REGULATION OF LYMPHOCYTE PROLIFERATION',
        'REGULATION OF LYMPHOCYTE ACTIVATION',
        'IMMUNE EFFECTOR PROCESS',
        'INTERFERON SIGNALING',
        'INTERFERON GAMMA SIGNALING',
        'INTERLEUKIN-12 FAMILY SIGNALING',
        'INTERLEUKIN-10 SIGNALING',
        'POSITIVE REGULATION OF LYMPHOCYTE MIGRATION',
        'T CELL DIFFERENTIATION INVOLVED IN IMMUNE RESPONSE',
        'INTERLEUKIN-3, 5 AND GM-CSF SIGNALING',
        'LYMPHOCYTE COSTIMULATION',
        'LYMPHOCYTE PROLIFERATION',
        'INTERLEUKIN-2 SIGNALING')

y_pos = np.arange(len(bars))

# Create horizontal bars
plt.barh(y_pos, height, color=['blue','blue','blue','blue','blue','blue','blue', 'red', 'red','red','red','red','red'])
plt.xlabel('NES',fontsize=15, fontname="sans-serif", fontweight="bold")
# Create names on the y-axis
plt.yticks(y_pos, bars)
red_patch = mpatches.Patch(color='red', label='Irf8KO')
blue_patch = mpatches.Patch(color='blue', label='Irf8WT')
plt.legend(handles=[red_patch,blue_patch])
plt.title('ImmununoSignature Gene Set Enrichment',fontsize=15, fontname="sans-serif", fontweight="bold")
#plt.show()
plt.savefig('/Users/simonepuccio/Documents/HumanitasProjects/SP006_Irf8/Immuno.pdf', format='pdf',
            bbox_inches='tight', dpi=300)
