import eurostat
toc_df = eurostat.get_toc_df()
print(toc_df)
f = eurostat.subset_toc_df(toc_df,'fleet')
print(f)