#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__G__em__ep__G__u__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__u__G__em__ep__G__u__S4_1(bs);
}

V2_4__u__G__em__ep__G__u__S4_1::V2_4__u__G__em__ep__G__u__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[568];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__u__G__em__ep__G__u__S4_1::~V2_4__u__G__em__ep__G__u__S4_1()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<64;i++) delete[] M[i];
    delete[] M;
  }
}

Complex V2_4__u__G__em__ep__G__u__S4_1::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 2: Calculate_M2(); break;
    case 3: Calculate_M3(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 14: Calculate_M14(); break;
    case 15: Calculate_M15(); break;
    case 16: Calculate_M16(); break;
    case 17: Calculate_M17(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 28: Calculate_M28(); break;
    case 29: Calculate_M29(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
    case 32: Calculate_M32(); break;
    case 33: Calculate_M33(); break;
    case 34: Calculate_M34(); break;
    case 35: Calculate_M35(); break;
    case 44: Calculate_M44(); break;
    case 45: Calculate_M45(); break;
    case 46: Calculate_M46(); break;
    case 47: Calculate_M47(); break;
    case 48: Calculate_M48(); break;
    case 49: Calculate_M49(); break;
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 60: Calculate_M60(); break;
    case 61: Calculate_M61(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M0()
{
  M[0][0] = (Z[19]*Z[18]+Z[46]*Z[45])*Z[62];
  M[0][1] = -Z[94]*Z[13]*Z[89];
  M[0][2] = -(Z[19]*Z[105]+Z[46]*Z[110])*Z[114];
  M[0][3] = -(Z[132]*Z[70]+Z[140]*Z[76])*Z[146];
  M[0][4] = -(Z[153]*Z[36]+Z[150]*Z[8]-Z[148]*Z[98])*Z[154];
  M[0][5] = -Z[164]*Z[109]*Z[160];
  M[0][6] = (Z[174]*Z[173]-Z[166]*Z[165])*Z[179];
  M[0][7] = Z[206]*Z[109]*Z[200];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M1()
{
  M[1][0] = (Z[19]*Z[208]+Z[46]*Z[210])*Z[62];
  M[1][1] = -Z[94]*Z[207]*Z[89];
  M[1][2] = -(Z[19]*Z[212]+Z[46]*Z[214])*Z[114];
  M[1][3] = -(Z[224]*Z[70]+Z[230]*Z[76])*Z[146];
  M[1][4] = -(Z[153]*Z[40]+Z[150]*Z[12]-Z[148]*Z[183])*Z[154];
  M[1][5] = -Z[164]*Z[109]*Z[236];
  M[1][6] = (Z[238]*Z[173]-Z[166]*Z[170])*Z[179];
  M[1][7] = Z[206]*Z[109]*Z[242];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M2()
{
  M[2][0] = (Z[19]*Z[246]+Z[46]*Z[248])*Z[62];
  M[2][1] = -Z[94]*Z[244]*Z[78];
  M[2][2] = -(Z[19]*Z[253]+Z[46]*Z[258])*Z[114];
  M[2][3] = -(Z[266]*Z[70]+Z[269]*Z[76])*Z[146];
  M[2][4] = -(Z[274]*Z[36]+Z[273]*Z[8]-Z[272]*Z[98])*Z[154];
  M[2][5] = -(Z[257]*Z[160]-Z[256]*Z[157])*Z[164];
  M[2][6] = Z[179]*Z[174]*Z[284];
  M[2][7] = (Z[257]*Z[200]-Z[256]*Z[187])*Z[206];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M3()
{
  M[3][0] = (Z[19]*Z[288]+Z[46]*Z[290])*Z[62];
  M[3][1] = -Z[94]*Z[244]*Z[85];
  M[3][2] = -(Z[19]*Z[292]+Z[46]*Z[294])*Z[114];
  M[3][3] = -(Z[298]*Z[70]+Z[300]*Z[76])*Z[146];
  M[3][4] = -(Z[274]*Z[40]+Z[273]*Z[12]-Z[272]*Z[183])*Z[154];
  M[3][5] = -(Z[257]*Z[236]-Z[256]*Z[234])*Z[164];
  M[3][6] = (Z[238]*Z[284]-Z[166]*Z[281])*Z[179];
  M[3][7] = (Z[257]*Z[242]-Z[256]*Z[240])*Z[206];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M12()
{
  M[12][0] = (Z[19]*Z[311]+Z[46]*Z[331])*Z[62];
  M[12][1] = -Z[94]*Z[13]*Z[350];
  M[12][2] = -(Z[19]*Z[357]+Z[46]*Z[359])*Z[114];
  M[12][3] = -(Z[124]*Z[344]+Z[140]*Z[347])*Z[146];
  M[12][4] = -(Z[153]*Z[324]+Z[150]*Z[304]-Z[148]*Z[353])*Z[154];
  M[12][5] = -Z[164]*Z[109]*Z[363];
  M[12][6] = (Z[174]*Z[367]-Z[166]*Z[365])*Z[179];
  M[12][7] = Z[206]*Z[109]*Z[383];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M13()
{
  M[13][0] = (Z[19]*Z[388]+Z[46]*Z[390])*Z[62];
  M[13][1] = -Z[94]*Z[207]*Z[350];
  M[13][2] = -(Z[19]*Z[392]+Z[46]*Z[394])*Z[114];
  M[13][3] = -(Z[218]*Z[344]+Z[230]*Z[347])*Z[146];
  M[13][4] = -(Z[153]*Z[327]+Z[150]*Z[307]-Z[148]*Z[370])*Z[154];
  M[13][5] = -Z[164]*Z[109]*Z[398];
  M[13][6] = (Z[238]*Z[367]-Z[166]*Z[366])*Z[179];
  M[13][7] = Z[206]*Z[109]*Z[402];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M14()
{
  M[14][0] = (Z[19]*Z[404]+Z[46]*Z[406])*Z[62];
  M[14][1] = -Z[94]*Z[244]*Z[348];
  M[14][2] = -(Z[19]*Z[408]+Z[46]*Z[410])*Z[114];
  M[14][3] = -(Z[263]*Z[344]+Z[269]*Z[347])*Z[146];
  M[14][4] = -(Z[274]*Z[324]+Z[273]*Z[304]-Z[272]*Z[353])*Z[154];
  M[14][5] = -(Z[257]*Z[363]-Z[256]*Z[361])*Z[164];
  M[14][6] = Z[179]*Z[174]*Z[413];
  M[14][7] = (Z[257]*Z[383]-Z[256]*Z[373])*Z[206];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M15()
{
  M[15][0] = (Z[19]*Z[414]+Z[46]*Z[416])*Z[62];
  M[15][1] = -Z[94]*Z[244]*Z[349];
  M[15][2] = -(Z[19]*Z[418]+Z[46]*Z[420])*Z[114];
  M[15][3] = -(Z[296]*Z[344]+Z[300]*Z[347])*Z[146];
  M[15][4] = -(Z[274]*Z[327]+Z[273]*Z[307]-Z[272]*Z[370])*Z[154];
  M[15][5] = -(Z[257]*Z[398]-Z[256]*Z[396])*Z[164];
  M[15][6] = (Z[238]*Z[413]-Z[166]*Z[412])*Z[179];
  M[15][7] = (Z[257]*Z[402]-Z[256]*Z[400])*Z[206];
}

void V2_4__u__G__em__ep__G__u__S4_1::Calculate_M16()
{
  M[16][0] = (Z[422]*Z[18]+Z[423]*Z[45])*Z[62];
  M[16][1] = -Z[94]*Z[13]*Z[441];
  M[16][2] = -(Z[422]*Z[105]+Z[423]*Z[110])*Z[114];
  M[16][3] = -(Z[450]*Z[70]+Z[452]*Z[76])*Z[146];
  M[16][4] = -(Z[456]*Z[36]+Z[455]*Z[8]-Z[454]*Z[98])*Z[154];
  M[16][5] = -Z[164]*Z[109]*Z[462];
  M[16][6] = (Z[466]*Z[173]-Z[465]*Z[165])*Z[179];
  M[16][7] = Z[206]*Z[109]*Z[470];
}

