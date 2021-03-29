# {{ cookiecutter.project_name }} - Data
Put raw, interim and processed data in the respective folders.  
Make sure to manage all data with [Git LFS](https://git-lfs.github.com/)  
Interim and processed data must be saved in [parquet](https://parquet.apache.org/documentation/latest/) format

## Example
Track CSV files with Git LFS:

    git lfs track "*.csv"
Add *.gitattributes* to source control:

    git add .gitattributes
Work with large CSV files as usual:

    git add large.csv
    git commit -m "Add large CSV"
    git push