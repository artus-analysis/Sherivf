#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__d__db__em__ep__G__G__S4_0(Basic_Sfuncs* bs) {
  return new V2_4__d__db__em__ep__G__G__S4_0(bs);
}

V2_4__d__db__em__ep__G__G__S4_0::V2_4__d__db__em__ep__G__G__S4_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[578];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__d__db__em__ep__G__G__S4_0::~V2_4__d__db__em__ep__G__G__S4_0()
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

Complex V2_4__d__db__em__ep__G__G__S4_0::Evaluate(int m,int n)
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

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M0()
{
  M[0][0] = Z[43]*Z[38]*Z[37];
  M[0][1] = -Z[84]*Z[38]*Z[73];
  M[0][2] = (Z[49]*Z[111]-Z[44]*Z[100])*Z[116];
  M[0][3] = -(Z[124]*Z[8]+Z[126]*Z[17]-Z[129]*Z[26])*Z[131];
  M[0][4] = -(Z[143]*Z[91]-Z[151]*Z[97])*Z[156];
  M[0][5] = -(Z[35]*Z[158]-Z[36]*Z[161])*Z[165];
  M[0][6] = (Z[35]*Z[175]-Z[36]*Z[188])*Z[195];
  M[0][7] = (Z[171]*Z[206]-Z[166]*Z[196])*Z[209];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M1()
{
  M[1][0] = Z[43]*Z[38]*Z[212];
  M[1][1] = -Z[84]*Z[38]*Z[218];
  M[1][2] = (Z[214]*Z[111]-Z[44]*Z[107])*Z[116];
  M[1][3] = -(Z[124]*Z[170]+Z[126]*Z[48]-Z[129]*Z[68])*Z[131];
  M[1][4] = -(Z[228]*Z[91]-Z[234]*Z[97])*Z[156];
  M[1][5] = -(Z[35]*Z[238]-Z[36]*Z[240])*Z[165];
  M[1][6] = (Z[35]*Z[243]-Z[36]*Z[245])*Z[195];
  M[1][7] = (Z[242]*Z[206]-Z[166]*Z[203])*Z[209];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M2()
{
  M[2][0] = -(Z[162]*Z[34]-Z[38]*Z[40])*Z[43];
  M[2][1] = (Z[162]*Z[64]-Z[38]*Z[82])*Z[84];
  M[2][2] = (Z[54]*Z[257]-Z[44]*Z[255])*Z[116];
  M[2][3] = -(Z[259]*Z[12]+Z[261]*Z[21]-Z[129]*Z[30])*Z[131];
  M[2][4] = -(Z[139]*Z[250]-Z[155]*Z[254])*Z[156];
  M[2][5] = -(Z[39]*Z[160]-Z[36]*Z[163])*Z[165];
  M[2][6] = (Z[39]*Z[183]-Z[36]*Z[193])*Z[195];
  M[2][7] = -Z[209]*Z[166]*Z[262];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M3()
{
  M[3][0] = -(Z[162]*Z[211]-Z[38]*Z[213])*Z[43];
  M[3][1] = (Z[162]*Z[217]-Z[38]*Z[219])*Z[84];
  M[3][2] = (Z[215]*Z[257]-Z[44]*Z[256])*Z[116];
  M[3][3] = -(Z[259]*Z[179]+Z[261]*Z[59]-Z[129]*Z[77])*Z[131];
  M[3][4] = -(Z[225]*Z[250]-Z[237]*Z[254])*Z[156];
  M[3][5] = -(Z[39]*Z[239]-Z[36]*Z[241])*Z[165];
  M[3][6] = (Z[39]*Z[244]-Z[36]*Z[246])*Z[195];
  M[3][7] = -Z[209]*Z[166]*Z[263];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M12()
{
  M[12][0] = Z[43]*Z[38]*Z[285];
  M[12][1] = -Z[84]*Z[38]*Z[307];
  M[12][2] = (Z[49]*Z[323]-Z[44]*Z[321])*Z[116];
  M[12][3] = -(Z[124]*Z[267]+Z[126]*Z[273]-Z[129]*Z[279])*Z[131];
  M[12][4] = -(Z[135]*Z[317]-Z[151]*Z[320])*Z[156];
  M[12][5] = -(Z[35]*Z[324]-Z[36]*Z[326])*Z[165];
  M[12][6] = (Z[35]*Z[333]-Z[36]*Z[343])*Z[195];
  M[12][7] = (Z[171]*Z[350]-Z[166]*Z[348])*Z[209];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M13()
{
  M[13][0] = Z[43]*Z[38]*Z[353];
  M[13][1] = -Z[84]*Z[38]*Z[357];
  M[13][2] = (Z[214]*Z[323]-Z[44]*Z[322])*Z[116];
  M[13][3] = -(Z[124]*Z[330]+Z[126]*Z[289]-Z[129]*Z[303])*Z[131];
  M[13][4] = -(Z[222]*Z[317]-Z[234]*Z[320])*Z[156];
  M[13][5] = -(Z[35]*Z[359]-Z[36]*Z[361])*Z[165];
  M[13][6] = (Z[35]*Z[363]-Z[36]*Z[365])*Z[195];
  M[13][7] = (Z[242]*Z[350]-Z[166]*Z[349])*Z[209];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M14()
{
  M[14][0] = -(Z[162]*Z[284]-Z[38]*Z[286])*Z[43];
  M[14][1] = (Z[162]*Z[300]-Z[38]*Z[314])*Z[84];
  M[14][2] = (Z[54]*Z[374]-Z[44]*Z[372])*Z[116];
  M[14][3] = -(Z[259]*Z[270]+Z[261]*Z[276]-Z[129]*Z[282])*Z[131];
  M[14][4] = -(Z[147]*Z[369]-Z[155]*Z[371])*Z[156];
  M[14][5] = -(Z[39]*Z[325]-Z[36]*Z[327])*Z[165];
  M[14][6] = (Z[39]*Z[339]-Z[36]*Z[347])*Z[195];
  M[14][7] = -Z[209]*Z[166]*Z[375];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M15()
{
  M[15][0] = -(Z[162]*Z[352]-Z[38]*Z[354])*Z[43];
  M[15][1] = (Z[162]*Z[356]-Z[38]*Z[358])*Z[84];
  M[15][2] = (Z[215]*Z[374]-Z[44]*Z[373])*Z[116];
  M[15][3] = -(Z[259]*Z[336]+Z[261]*Z[296]-Z[129]*Z[310])*Z[131];
  M[15][4] = -(Z[231]*Z[369]-Z[237]*Z[371])*Z[156];
  M[15][5] = -(Z[39]*Z[360]-Z[36]*Z[362])*Z[165];
  M[15][6] = (Z[39]*Z[364]-Z[36]*Z[366])*Z[195];
  M[15][7] = -Z[209]*Z[166]*Z[376];
}

void V2_4__d__db__em__ep__G__G__S4_0::Calculate_M16()
{
  M[16][0] = Z[43]*Z[38]*Z[387];
  M[16][1] = -Z[84]*Z[38]*Z[395];
  M[16][2] = (Z[391]*Z[111]-Z[390]*Z[100])*Z[116];
  M[16][3] = -(Z[400]*Z[8]+Z[401]*Z[17]-Z[402]*Z[26])*Z[131];
  M[16][4] = -(Z[408]*Z[91]-Z[412]*Z[97])*Z[156];
  M[16][5] = -(Z[385]*Z[158]-Z[386]*Z[161])*Z[165];
  M[16][6] = (Z[385]*Z[175]-Z[386]*Z[188])*Z[195];
  M[16][7] = (Z[171]*Z[425]-Z[166]*Z[415])*Z[209];
}

