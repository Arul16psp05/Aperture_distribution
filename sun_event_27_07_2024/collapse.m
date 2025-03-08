
clf
clear
load sun_event_spectrums_27_07_2024.mat
sp=spectrums(1:43200,1:255);

 
 clear csp
 csp(1:433,1:255) = 0;
 
idx2=1

for idx=1:100:(43200)

 idx

 for jdx=0:99
   csp(idx2,1:255) = csp(idx2,1:255) .+ sp(idx+jdx,1:255);
 end;
 idx2++
 end;
 
 pl=(csp/1e15);
 
 pl200=pl(200:270,:);
 
 rcsp(1:433,1:64) = 0;
 
idx2=1

for idx=1:4:(252)

 idx

 for jdx=0:4
   rcsp(:,idx2) = rcsp(:,idx2) .+ pl(:,idx+jdx);
 end;
 idx2++
 end;
 
  rpl200=pl(200:270,:);
  #%contour((rpl200'),511);
#  contour((3*(rpl200')),1111);
   # contour((10*(rpl200')),1111);
#   contour((30*(rpl200')),1111);
#      contour((50*(rpl200')),1111);
      contour((5000*(rpl200')),1111);
      
colorbar
xlabel('time')
ylabel('Frequncy')
 title('SUN Event 27-July-2024')
 
 
 save plotr50.png

