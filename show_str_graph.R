# auther: xulingjiang
# time: 2022/6/15
# coding: utf-8

windowsFonts(KT = windowsFont("楷体"))        # 添加楷体字体，防止中文字符无法输出

# 设置生成图片路径即其格式
setwd("C:/Users/18282/Desktop/Python/Nsep")
png("Graph.png")

# 读入csv文件，并将表头赋予顺序数字
str_mat <- read.csv("C:/Users/18282/Desktop/Python/Nsep/mat.csv"
                    ,header = FALSE,encoding = 'UTF-8')
colnames(str_mat) <- c(1:length(str_mat))

# 绘制空图及节点，并在节点顺序标号
r <- 3; d <- r/30
plot(c(1:length(str_mat)),rep(0,length(str_mat)),pch=1,cex=r
     ,xaxt='n',yaxt='n',ann=FALSE,bty='n'
     ,xlim=c(1,length(str_mat)),ylim=c(-2,2))
for(i in 1:length(str_mat)){text(i, 0, as.character(i-1), cex=r/3)}

# 根据csv，绘制有向边，在边上添加相应字符串。
arr <- function(i,j,y){
  if(j-i > 1){
    arrows(i, d * sym, 0.2+i, y, angle=0, length=0.15, lty=6)
    arrows(0.2+i, y, j-0.2, y, angle=0, length=0.15, lty=6)
    arrows(j-0.2, y, j, d * sym, angle=20,length=0.15, lty=6)
  }
  else{
    arrows(i + d, 0, j - d, 0, angle=15,length=0.15, lty=6)
  }
}
for(i in 1:length(str_mat)){
  for(j in 1:length(str_mat)){
    if(str_mat[i,j] != '0'){
      x <- (j+i) / 2
      if(i %% 2==0){sym = -1}else{sym = 1}
      # print(sym)
      y <- ((j-i-1) * sym) / 2
      arr(i,j,y)
      text(x,y,labels=str_mat[i,j],pos=3, col='azure4',family='KT')
    }
  }
}

# 图片生成结束，打印成功消息
dev.off()
print('the str_graph has generated in the Graph.png. ')
