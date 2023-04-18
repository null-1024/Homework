clc,clear;
I=imread("D:\桌面\24.bmp");
image=im2double(I);
acc=ones(size(image));
for row = 1:1:669
    for col = 1:1:343
        if( row==1 && col==1 )
            acc(row,col) = image(row,col);
        elseif( row==1)
            acc(row,col) = acc(row,col-1)+image(row,col);
        elseif( col==1 )
            acc(row,col) = acc(row-1,col)+image(row,col);
        else
            acc(row,col) = acc(row,col-1)-acc(row-1,col-1)+acc(row-1,col)+image(row,col);%二维前缀和
        end
    end
end
lowerboundary = acc(669,343)/(669*343);
pfa=0.23;
N=2;
G=1;
dr_col=3;
dr_row=1;
%length=7,width=3
for row = 1:1:669
    for col = 1:1:343
        nc=21;
        alpha=nc*(pfa^(-1/nc)-1);
        if(row<=2&&col<=4)
            sumn=acc(row+1,col+3);
        elseif(row<=2&&col<=340)
            sumn=acc(row+1,col+3)-acc(row+1,col-4);
        elseif(col<=4&&row<=668)
            sumn=acc(row+1,col+3)-acc(row-2,col+3);
        elseif(row>2&&col>4&&col<=340&&row<=668)
            sumn=acc(row+1,col+3)+acc(row-2,col-4)-acc(row-2,col+3)-acc(row+1,col-4);
        end
        if(row<=2&&col<=4)
            sumg=acc(row+1,col+1);
        elseif(row<=2&&col<=340)
            sumg=acc(row+1,col+1)-acc(row+1,col-2);
        elseif(col<=4&&row<=668)
            sumg=acc(row+1,col+1)-acc(row-2,col+1) ;
        elseif(row>2&&col>4&&col<=340&&row<=668)
            sumg=acc(row+1,col+1)+acc(row-2,col-2)-acc(row-2,col+1)-acc(row+1,col-2);
        end
        threshold=((sumn-sumg)/nc)*alpha;
        value=image(row,col);
        if (value>threshold && threshold>lowerboundary)
            image(row,col)=255;
        else
            image(row,col)=0;
        end
    end
end
imshow(image);

                    