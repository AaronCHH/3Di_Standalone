# Update forked repo
<!-- TOC -->

- [Update forked repo](#update-forked-repo)
  - [Check](#check)
  - [Add upstream repo](#add-upstream-repo)
  - [Check again](#check-again)
  - [Begin update](#begin-update)
  - [References](#references)

<!-- /TOC -->
## Check
```
$ git remote -v
```

預設應該只會有 origin 這個 remote：  
```
origin https://github.com/user/repo.git (fetch)  
origin https://github.com/user/repo.git (push)  
```

我們用下面這個命令來加入遠端的 repository，在這邊的情境也就是比較新的、上游的 repository
upstream 是 remote name、可以自己取名，不要重複就好，但後面我都用會 upstream 做示範
而後面那串網址是 repository 位置：

## Add upstream repo
```
$ git remote add upstream https://github.com/otheruser/repo.git
```

## Check again
如果再看一次現有的remote端應該會發現多了兩組 upstream (fetch & push)：
```
$ git remote -v
origin https://github.com/user/repo.git (fetch)
origin https://github.com/user/repo.git (push)
upstream https://github.com/otheruser/repo.git (fetch)
upstream https://github.com/otheruser/repo.git (push)
```

有了遠端的來源後我們就可以開始做更新了

假如我要做更新的的 branch 是 master 的話就先切到 master branch：

## Begin update
```
$ git checkout master
```
接著把 upstream 的 master 更新給拉進來
```
$ git pull upstream master
```
如果你的 master branch 有自己的 commit, 也可以用 rebase 來避免不必要的 merge 操作:
```
$ git pull --rebase upstream master
```
如果沒有發生衝突的話這樣應該就完成了本地的更新，再把更新後的 branch push 出去就行了
```
$ git push origin master
```
這時再回去看看你的 repository 頁面，應該會發現已經同步到最新的狀態了！

## References
* https://help.github.com/articles/syncing-a-fork
* https://help.github.com/articles/configuring-a-remote-for-a-fork/