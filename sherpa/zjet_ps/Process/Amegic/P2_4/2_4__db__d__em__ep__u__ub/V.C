#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__db__d__em__ep__u__ub(Basic_Sfuncs* bs) {
  return new V2_4__db__d__em__ep__u__ub(bs);
}

V2_4__db__d__em__ep__u__ub::V2_4__db__d__em__ep__u__ub(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[10];
  Z = new Complex[244];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__db__d__em__ep__u__ub::~V2_4__db__d__em__ep__u__ub()
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

Complex V2_4__db__d__em__ep__u__ub::Evaluate(int m,int n)
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

void V2_4__db__d__em__ep__u__ub::Calculate_M0()
{
  M[0][0] = -(Z[14]*Z[10]-Z[8]*Z[1])*Z[21];
  M[0][1] = (Z[28]*Z[27]+Z[1]*Z[32])*Z[35];
  M[0][2] = -(Z[1]*Z[39]+Z[44]*Z[43])*Z[48];
  M[0][3] = -(Z[62]*Z[61]-Z[53]*Z[52])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M1()
{
  M[1][0] = -(Z[14]*Z[79]-Z[8]*Z[77])*Z[21];
  M[1][1] = (Z[84]*Z[27]+Z[77]*Z[32])*Z[35];
  M[1][2] = -(Z[77]*Z[39]+Z[85]*Z[43])*Z[48];
  M[1][3] = -(Z[62]*Z[98]-Z[53]*Z[90])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M2()
{
  M[2][0] = -(Z[118]*Z[18]-Z[113]*Z[9])*Z[21];
  M[2][1] = (Z[120]*Z[27]+Z[9]*Z[32])*Z[35];
  M[2][2] = -(Z[9]*Z[39]+Z[121]*Z[43])*Z[48];
  M[2][3] = -(Z[123]*Z[74]-Z[53]*Z[57])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M3()
{
  M[3][0] = -(Z[118]*Z[82]-Z[113]*Z[78])*Z[21];
  M[3][1] = (Z[125]*Z[27]+Z[78]*Z[32])*Z[35];
  M[3][2] = -(Z[78]*Z[39]+Z[126]*Z[43])*Z[48];
  M[3][3] = -(Z[123]*Z[110]-Z[53]*Z[94])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M12()
{
  M[12][0] = -(Z[133]*Z[16]-Z[130]*Z[1])*Z[21];
  M[12][1] = (Z[23]*Z[136]+Z[1]*Z[139])*Z[35];
  M[12][2] = -(Z[1]*Z[142]+Z[46]*Z[145])*Z[48];
  M[12][3] = -(Z[62]*Z[154]-Z[53]*Z[148])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M13()
{
  M[13][0] = -(Z[133]*Z[81]-Z[130]*Z[77])*Z[21];
  M[13][1] = (Z[83]*Z[136]+Z[77]*Z[139])*Z[35];
  M[13][2] = -(Z[77]*Z[142]+Z[86]*Z[145])*Z[48];
  M[13][3] = -(Z[62]*Z[172]-Z[53]*Z[166])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M14()
{
  M[14][0] = -(Z[186]*Z[15]-Z[183]*Z[9])*Z[21];
  M[14][1] = (Z[119]*Z[136]+Z[9]*Z[139])*Z[35];
  M[14][2] = -(Z[9]*Z[142]+Z[122]*Z[145])*Z[48];
  M[14][3] = -(Z[123]*Z[163]-Z[53]*Z[151])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M15()
{
  M[15][0] = -(Z[186]*Z[80]-Z[183]*Z[78])*Z[21];
  M[15][1] = (Z[124]*Z[136]+Z[78]*Z[139])*Z[35];
  M[15][2] = -(Z[78]*Z[142]+Z[127]*Z[145])*Z[48];
  M[15][3] = -(Z[123]*Z[181]-Z[53]*Z[169])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M48()
{
  M[48][0] = -(Z[14]*Z[233]-Z[8]*Z[195])*Z[21];
  M[48][1] = (Z[212]*Z[190]+Z[195]*Z[194])*Z[35];
  M[48][2] = -(Z[195]*Z[216]+Z[197]*Z[221])*Z[48];
  M[48][3] = -(Z[238]*Z[70]-Z[237]*Z[52])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M49()
{
  M[49][0] = -(Z[14]*Z[239]-Z[8]*Z[198])*Z[21];
  M[49][1] = (Z[222]*Z[190]+Z[198]*Z[194])*Z[35];
  M[49][2] = -(Z[198]*Z[216]+Z[200]*Z[221])*Z[48];
  M[49][3] = -(Z[238]*Z[106]-Z[237]*Z[90])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M50()
{
  M[50][0] = -(Z[118]*Z[236]-Z[113]*Z[201])*Z[21];
  M[50][1] = (Z[224]*Z[190]+Z[201]*Z[194])*Z[35];
  M[50][2] = -(Z[201]*Z[216]+Z[203]*Z[221])*Z[48];
  M[50][3] = -(Z[243]*Z[66]-Z[237]*Z[57])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M51()
{
  M[51][0] = -(Z[118]*Z[242]-Z[113]*Z[204])*Z[21];
  M[51][1] = (Z[226]*Z[190]+Z[204]*Z[194])*Z[35];
  M[51][2] = -(Z[204]*Z[216]+Z[206]*Z[221])*Z[48];
  M[51][3] = -(Z[243]*Z[102]-Z[237]*Z[94])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M60()
{
  M[60][0] = -(Z[133]*Z[235]-Z[130]*Z[195])*Z[21];
  M[60][1] = (Z[213]*Z[209]+Z[195]*Z[211])*Z[35];
  M[60][2] = -(Z[195]*Z[229]+Z[196]*Z[232])*Z[48];
  M[60][3] = -(Z[238]*Z[160]-Z[237]*Z[148])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M61()
{
  M[61][0] = -(Z[133]*Z[241]-Z[130]*Z[198])*Z[21];
  M[61][1] = (Z[223]*Z[209]+Z[198]*Z[211])*Z[35];
  M[61][2] = -(Z[198]*Z[229]+Z[199]*Z[232])*Z[48];
  M[61][3] = -(Z[238]*Z[178]-Z[237]*Z[166])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M62()
{
  M[62][0] = -(Z[186]*Z[234]-Z[183]*Z[201])*Z[21];
  M[62][1] = (Z[225]*Z[209]+Z[201]*Z[211])*Z[35];
  M[62][2] = -(Z[201]*Z[229]+Z[202]*Z[232])*Z[48];
  M[62][3] = -(Z[243]*Z[157]-Z[237]*Z[151])*Z[76];
}

void V2_4__db__d__em__ep__u__ub::Calculate_M63()
{
  M[63][0] = -(Z[186]*Z[240]-Z[183]*Z[204])*Z[21];
  M[63][1] = (Z[227]*Z[209]+Z[204]*Z[211])*Z[35];
  M[63][2] = -(Z[204]*Z[229]+Z[205]*Z[232])*Z[48];
  M[63][3] = -(Z[243]*Z[175]-Z[237]*Z[169])*Z[76];
}

