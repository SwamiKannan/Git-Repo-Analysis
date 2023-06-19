# Git Repo Analysis
### Analysis of Git repo structures downloaded from Github
<p align='center'>
 <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/cover.png" size=30%>
 <sub>Image Credit: <a href="https://www.data-to-viz.com/graph/network_files/figure-html/unnamed-chunk-6-1.png">From Data to Viz</a></sub>
</p>

This project started while I was perusing other Github repositories. I was blown away by <a href="https://github.com/ggeop">Georgios Papachristou's</a> <a href="https://github.com/ggeop/Python-ai-assistant">git repo on an AI assistant</a>. However it was a huge struggle to figure where to start reading the code in the repo (Ironically, it was the Jarvis library). But that's where I decided to make this tool

## Functionality:
Analysis the folder structure of the git repo, identifies all .py files and builds a graph that shows which files call which other files.

## Operation:
<ul>
 <li>Extract start.py and the src folder to the main git repo</li>
 <li>Run:</li>
</ul>
```
python start.py
```

## Screenshots:
<ul>
 <li>Graphics results:</li>
</ul>

<table border="0 px" cellpadding="0" cellspacing="0">
 <thead>
<tr>
 <th> Repo folder structure</th>
 <th> Network graph </th> 
</tr>
 </thead>
 <tr>
  <td width=40%>
   <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/folder_structure.jpg" width="60%" />
  </td>
  <td border="0">
   <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/graph.jpg" width="100%"> 
  </td>
 </tr>
</table>
<br>

<br>
<ul>
<li>Command prompt results</li>
</ul>
<img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/outputs/output_called.PNG">
<img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/outputs/output_calling.PNG">

<ul>
 <li>JSON outputs:
  <ul>
  <li><a href="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/outputs/only_called.json">Functions that have only been called </a> </li>
 <li><a href="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/outputs/only_calling.json">Functions that have only called other libraries  / functions </a></li>
  </ul></li></ul>

## To-do:
Only parent folders are mapped right now. Need to add sub-folders to the mix.


