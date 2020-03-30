import numpy as np

# The result is a dictionary keyed on analysis, containing reports keyed on model id
# The console app is the recommended way to view these, by saving the results to file
# (see previous cell), but programmatic analysis of the result here is also possible

# Here we'll extract the frequency of feature usage in generated counterfactuals for each model
def get_feature_frequency(model_id, result):
    # Extract the information for fairness of a particular model id
    local_model_explanation_info = result['explanation'][model_id]
    # Extract the full set of counterfactuals for this
    all_counterfactuals = [ind for r in local_model_explanation_info['explanations'] for ind in r['bestIndividuals']]

    def features_changed(counterfactual):
        # Each feature has an entry saying how it changed.  This will be one of:
        #   'unchanged'
        #   'changed' (categorical change)
        #   <numeric> (differnce from original value for numeric feaure)
        def no_change(diff):
            return (diff == 'unchanged') or diff == 0
        try:
            diffs = counterfactual['diff']
            res=[idx for idx in range(len(diffs)) if not no_change(diffs[idx])]
        except:
            res=[]
        return res


    # Get the full list of model features from the schema
    features = local_model_explanation_info['model_schema']['feature_schemas']
    num_model_features = len(features)

    feature_names = np.array([f['name'] for f in features])
    
    # Count the changes for each feature across the dataset
    all_changes = np.zeros(num_model_features)
    for cf in all_counterfactuals:
        changed = features_changed(cf)
        for idx in changed:
            all_changes[idx] += 1
    return all_changes, feature_names

def plot_histogram(ax, model_id, result):
    all_changes, feature_names = get_feature_frequency(model_id, result)
    indexes = np.arange(len(all_changes))
    order = np.argsort(-all_changes)

    ax.bar(indexes,all_changes[order])

    ax.ylabel = 'Frequency'
    ax.set_title(f'Model: {model_id}')
    ax.set_xticks(indexes)
    ax.set_xticklabels(feature_names[order], rotation=90)