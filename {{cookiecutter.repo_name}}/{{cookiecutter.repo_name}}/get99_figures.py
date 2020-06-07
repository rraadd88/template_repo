# from rohan.global_imports import *

# def get01_plot_heatmap_dms(cfg,plot_heatmap_dmsp):
#     dplot=read_table(cfg['ddmsp'])
#     sns.heatmap(dplot.pivot_table(index='mutated',columns=['position','reference',],values='activity_score'),
#                cbar_kws={'label':'score'},cmap='RdBu_r',vmax=4,vmin=-4)
#     savefig(plot_heatmap_dmsp)

# def get01_plot_dist_secondary_structure_score(cfg,plot_dist_secondary_structure_scorep):
#     dplot=read_table(cfg['ddms_featsp'])
#     sns.violinplot(data=dplot,x='secondary structure',y='activity_score')
#     savefig(plot_dist_secondary_structure_scorep)

# def get01_plot_scatter_postion_score(cfg,plot_scatter_postion_scorep):
#     dplot=read_table(cfg['ddmsp'])
#     dplot.plot.scatter(y='activity_score',c='std',x='position',vmax=1)
#     savefig(plot_scatter_postion_scorep)
    