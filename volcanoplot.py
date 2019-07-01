import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# load data file
d = pd.read_csv("/Users/simonepuccio/Documents/HumanitasProjects/SP006_Irf8/volcanoplot_tableMouse.txt",
                sep="\t", header=0)

d.loc[(d['log2FoldChange'] >= 0.5) & (d['padj'] < 0.05), 'color'] = "red"  # upregulated
d.loc[(d['log2FoldChange'] < -0.5) & (d['padj'] < 0.05), 'color'] = "blue"   # downregulated
d['color'].fillna('lightgrey', inplace=True) # intermediate

plt.text(0.77, 12.011, "Irf8")
d['logpv']=-(np.log10(d['padj']))
plt.scatter(d['log2FoldChange'], d['logpv'], c=d['color'],s=3)
plt.xlim(-3, 3)
plt.ylim(0, 20)
plt.xlabel('log2 Fold Change',fontsize=15, fontname="sans-serif", fontweight="bold")
plt.ylabel('-log10(Q-value)', fontsize=15, fontname="sans-serif", fontweight="bold")
plt.xticks(fontsize=12, fontname="sans-serif")
plt.yticks(fontsize=12, fontname="sans-serif")
plt.axhline(1.3010, color='black', lw=1,linestyle="dashed")
plt.axvline(0.5, color='black', lw=1,linestyle="dashed")
plt.axvline(-0.5, color='black', lw=1,linestyle="dashed")
#plt.show()
plt.savefig('/Users/simonepuccio/Documents/HumanitasProjects/SP006_Irf8/Mouse_volcanoplot1.pdf', format='pdf', bbox_inches='tight', dpi=300)


# load data file
f = pd.read_csv("/Users/simonepuccio/Documents/HumanitasProjects/SP006_Irf8/MouseIrf8ko_wt_volcanoplot.txt",sep="\t", header=0)

f.loc[(f['log2FoldChange'] >= 0.5) & (f['padj'] < 0.05), 'color'] = "red"  # upregulated
f.loc[(f['log2FoldChange'] < -0.5) & (f['padj'] < 0.05), 'color'] = "blue"   # downregulated
f['color'].fillna('lightgrey', inplace=True) # intermediate

#plt.text(-0.50, 0.5, "Irf8")
f['logpv']=-(np.log10(f['padj']))
plt.scatter(f['log2FoldChange'], f['logpv'], c=f['color'],s=3)
plt.xlabel('log2 Fold Change',fontsize=15, fontname="sans-serif", fontweight="bold")
plt.ylabel('-log10(Q-value)', fontsize=15, fontname="sans-serif", fontweight="bold")
plt.xticks(fontsize=12, fontname="sans-serif")
plt.yticks(fontsize=12, fontname="sans-serif")
plt.axhline(1.3010, color='black', lw=1,linestyle="dashed")
plt.axvline(0.5, color='black', lw=1,linestyle="dashed")
plt.axvline(-0.5, color='black', lw=1,linestyle="dashed")
plt.show()
#plt.savefig('/Users/simonepuccio/Documents/HumanitasProjects/SP006_Irf8/Mouse_trs_volcanoplot1.pdf', format='pdf', bbox_inches='tight', dpi=300)

