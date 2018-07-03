import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("Dataset:")
print (df)
choice1 = input("\n\n1. Data Cleaning\n2. Data Transformation\n0. Exit\nEnter your choice:")
while (choice1!='0'):
    if (choice1=='1'):
        choice2=input("\n1. Filter out missing data in rows\n2. Filter out missing data in columns\n3. Filling in missing Data\n0. Exit\nEnter your choice:")
        if(choice2=='1'):
            print(df.dropna())
        elif(choice2=='2'):
            print(print(df.dropna(axis=1)))
        elif(choice2=='3'):
            print(df.fillna(df.mean()))
        else:
            print("Bye")
            choice1 = input("1. Data Cleaning\n2. Data Transformation\n0. Exit\nEnter your choice:")
    elif(choice1=='2'):
        choice2=input("\n1. Remove Dulpicate rows\n2. Count missing data using function\n3. Mapping data\n4. Fill Nan values\n5. Replacing a value in dataset\n6. Renaming Axis indexes\n7. Discretization and Binning\n8. Detecting and FilteringOutliers\n9. Random and Sampling Data\n0. Exit\nEnter your choice:")
        if(choice2=='1'):
            df['is_duplicated'] = df.duplicated(['one'])
            print("\nDataset showing Duplicate rows\n",df)
            print("\nTotal duplicate rows:",df['is_duplicated'].sum())
            df_nodup = df.loc[df['is_duplicated'] == False]
            print("\nDataset after removing duplicate rows:\n",df_nodup)
        elif(choice2=='2'):
            def num_missing(x):
                return sum(x.isnull())
            print("Missing values per column:")
            print(df.apply(num_missing, axis=0))
            print("\nMissing values per row:")
            print(df.apply(num_missing, axis=1))
        elif(choice2=='3'):
            x = pd.Series([1, 2, 3], index=['one', 'two', 'three'])
            print(x)
            y = pd.Series(['foo', 'bar', 'baz'], index=[1, 2, 3])
            print(y)
            print(x.map(y))
        elif(choice2=='4'):
            print("Replacing NaN value:")
            print(df.fillna(method='pad'))
        elif(choice2=='5'):
            replace_value=float(input("Enter value to be replaced:"))
            value=float(input("Enter new value:"))
            print(df.replace({replace_value:value}))
        elif(choice2=='6'):
            print("\nRenaming row name:\n")
            print(df.rename_axis("foo"))
            print("\nRenaming column name:\n")
            print(df.rename_axis("bar", axis="columns"))
        elif(choice2=='7'):
            def binning(col, cut_points):
            # Define min and max values:
                minval = col.min()
                maxval = col.max()
                break_points = [minval] + cut_points + [maxval]
                colBin = pd.cut(col, bins=break_points)
                return colBin
            cut_points = [0.0,0.2,0.4,0.6]
            df["Binning"] = binning(df["three"], cut_points)
            print(df)
        elif(choice2=='8'):
            print("\nFor column one:")
            print(df['one'][np.abs(df.one - df.one.mean()) <= (0.6 * df.one.std())])
            print("\nFor column two:")
            print(df['two'][np.abs(df.two - df.two.mean()) <= (0.6 * df.two.std())])
            print("\nFor column three:")
            print(df['three'][np.abs(df.three - df.three.mean()) <= (0.6 *
            df.three.std())])
        elif(choice2=='9'):
            rows = np.random.sample(10)
            df_3 = df.ix[rows]
            print("\nSampling data:\n",df_3)
            rows = np.random.choice(df.index.values, 10)
            sampled_df = df.ix[rows]
            print("Random selection:\n",sampled_df)
        else:
            print("Bye")
            choice1 = input("1. Data Cleaning\n2. Data Transformation\n0. Exit\nEnter your choice:")
    else:
        print("Wrong Input")
        exit()
