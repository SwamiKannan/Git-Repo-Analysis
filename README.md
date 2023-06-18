# Git Repo Analysis
### Analysis of Git repo structures downloaded from Github
<p align='center'>
 <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/cover.png" size=30%>
 <sub>Image Credit: <a href="https://www.data-to-viz.com/graph/network_files/figure-html/unnamed-chunk-6-1.png">From Data to Viz</a></sub>
</p>

This project started while I was perusing other Github repositories. I was blown away by <a href="https://github.com/ggeop">Georgios Papachristou's</a> <a href="https://github.com/ggeop/Python-ai-assistant">git repo on an AI assistant</a>. However it was a huge struggle to figure where to start reading the code in the repo (Ironically, it was the Jarvis library). But that's where I decided to make this tool
<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clearfix (clear floats) */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
## Functionality:
Analysis the folder structure of the git repo, identifies all .py files and builds a graph that shows which files call which other files.

# Screenshots:
<!--
Original:
<img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/folder_structure.PNG">
Final
<img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/graph.jpg" width=100%>
-->
<p float="center">
<b>Repo structure</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Repo structure</b>
  
  
</p>
<p float="left">
  
  <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/folder_structure.PNG" width="30%" />
  <img src="https://github.com/SwamiKannan/Git-Repo-Analysis/blob/main/graph.jpg" width="65%" /> 
</p>







## To-do:
Only parent folders are mapped right now. Need to add sub-folders to the mix.


