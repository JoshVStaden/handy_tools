import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def _variable_factor_map(X, figsize, sup, pca_values):
    (pca_values, explained_variance) = pca_values
    x=np.linspace(start=-1,stop=1,num=500)
    #Find y1 and y2 for these points
    y_positive=lambda x: np.sqrt(1-x**2) 
    y_negative=lambda x: -np.sqrt(1-x**2)
    plt.plot(x,list(map(y_positive, x)), color='maroon')
    plt.plot(x,list(map(y_negative, x)),color='maroon')

    #Plot smaller circle
    x=np.linspace(start=-0.5,stop=0.5,num=500)
    y_positive=lambda x: np.sqrt(0.5**2-x**2) 
    y_negative=lambda x: -np.sqrt(0.5**2-x**2)
    plt.plot(x,list(map(y_positive, x)), color='maroon')
    plt.plot(x,list(map(y_negative, x)),color='maroon')

    #Create broken lines
    x=np.linspace(start=-1,stop=1,num=30)
    plt.scatter(x,[0]*len(x), marker='_',color='maroon')
    plt.scatter([0]*len(x), x, marker='|',color='maroon')

    #Define color list
    colors = ['blue', 'red', 'green', 'black', 'purple', 'brown']
    if len(pca_values[0]) > 6:
        colors=colors*(int(len(pca_values[0])/6)+1)
    add_string=""
    for i in range(len(pca_values[0])):
        xi=pca_values[0][i]
        yi=pca_values[1][i]
        plt.arrow(0,0, 
                dx=xi, dy=yi, 
                head_width=0.03, head_length=0.03, 
                color=colors[i], length_includes_head=True)
        add_string=f" ({round(xi,2)} {round(yi,2)})"
        plt.text(pca_values[0, i], 
                pca_values[1, i] , 
                s=add_string )
    plt.xlabel(f"Component 1 ({round(explained_variance[0]*100,2)}%)")
    plt.ylabel(f"Component 2 ({round(explained_variance[1]*100,2)}%)")
    plt.title('Variable factor map (PCA)')

def _scree_plot(X, pca_values):
    pca_values, explained_variance = pca_values
    PC_vals = np.arange(len(pca_values)) + 1
    plt.plot(PC_vals, explained_variance, 'ro-', linewidth=2)
    plt.title("Scree Plot")
    plt.xlabel('Principal Component')
    plt.ylabel('Proportion of Explained Variance')
    

def visualize_data(df,y, opts, pca_values=None):
    df = pd.DataFrame(df)
    colnames = []
    for col in df.columns:
        colnames.append("f_%s" %col)
    df.columns = colnames
    # TODO: visualize the data
    for opt in opts.split(','):
        if opt == 'vfm':
            if pca_values is not None:
                plt.figure()
                _variable_factor_map(df, (15, 15), "Explained Variance", pca_values)
            else:
                raise Exception("PCA Values must be supplied for VFM")
        elif opt == 'scree':
            if pca_values is not None:
                plt.figure()
                _scree_plot(df, pca_values)
            else:
                raise Exception("PCA Values must be supplied for Scree Plot")
        elif opt == 'pair':
            sns.pairplot(df)
        elif opt=='swarm':
            sns.swarmplot(x=df.columns[1], y=df.columns[2], hue=y, data=df)
        elif opt == 'heatmap':
            sns.heatmap(df.corr(), annot=True)
        elif opt == 'clustermap':
            sns.clustermap(df.corr(), annot=True)
        else:
            print("Unkown Visualization ", opt)
    plt.show()