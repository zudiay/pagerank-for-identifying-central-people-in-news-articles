# PageRank for Identifying Central People in News Articles

Implementation of PageRank-based method to identify the most important people occurring in news articles.

The Reuters-21578 data set is used. Reuters-21578 contains 21578 news stories from Reuters newswire. There are 22 SGML files, each containing 1000 news articles, except the last file, which contains 578 articles. . There are a total of 118 topics (classes) and each article is classified into one or more topics

The data.txt file contains an undirected
and unweighted graph of social network of co-occurrence in news articles. The graph has been
constructed from a subset of 3000 news articles from the Reuters-21578 corpus by identifying the
person names. The vertices of the graph are defined as distinct people. An edge is constructed
between two people if their names appear in the same news article. The resulting social network
consists of 459 nodes and 1422 edges.

The power iteration method is used in the PageRank algorithm. Teleportation rate is taken as 0.15. 

### Running the program
- Python version
```Python 3.10.0```

- Place the input file with the same folder as the main.py file.
- Open terminal at that folder.
- Run the following command by replacing the <file_name> with your input file name.
```python3 main.py <file_name>```
- Example:
```python3 main.py data.txt```

<i> Developed for CMPE493 Introduction to Information Retrieval course, Bogazici University, Fall 2021 <i>
