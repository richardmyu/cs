#include <stdio.h>

main()
{int s[]={1,2,1,3,4,2,1,1};
int v[4]={0,0,0,0},k,i;
for (k=0;s[k];k++){
	switch(s[k]){
		case 1:i=0;
		case 2:i=1;
		case 3:i=2;
		case 4:i=3;
	}
	v[i]++;
}
for(k=0;k<4;k++){
	printf("%d ",v[k]);
}
}
