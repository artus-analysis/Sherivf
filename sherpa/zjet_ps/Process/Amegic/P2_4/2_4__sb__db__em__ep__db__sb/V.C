#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__sb__db__em__ep__db__sb(Basic_Sfuncs* bs) {
  return new V2_4__sb__db__em__ep__db__sb(bs);
}

V2_4__sb__db__em__ep__db__sb::V2_4__sb__db__em__ep__db__sb(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[7];
  Z = new Complex[244];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__sb__db__em__ep__db__sb::~V2_4__sb__db__em__ep__db__sb()
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

Complex V2_4__sb__db__em__ep__db__sb::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
    case 32: Calculate_M32(); break;
    case 33: Calculate_M33(); break;
    case 44: Calculate_M44(); break;
    case 45: Calculate_M45(); break;
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M0()
{
  M[0][0] = -(Z[8]*Z[1]+Z[14]*Z[10])*Z[21];
  M[0][1] = -(Z[26]*Z[22]+Z[35]*Z[31])*Z[49];
  M[0][2] = (Z[56]*Z[52]-Z[60]*Z[1])*Z[63];
  M[0][3] = -(Z[67]*Z[1]+Z[72]*Z[68])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M1()
{
  M[1][0] = -(Z[8]*Z[77]+Z[14]*Z[79])*Z[21];
  M[1][1] = -(Z[86]*Z[22]+Z[94]*Z[31])*Z[49];
  M[1][2] = (Z[56]*Z[108]-Z[60]*Z[77])*Z[63];
  M[1][3] = -(Z[67]*Z[77]+Z[72]*Z[109])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M12()
{
  M[12][0] = -(Z[127]*Z[1]+Z[130]*Z[16])*Z[21];
  M[12][1] = -(Z[133]*Z[22]+Z[139]*Z[31])*Z[49];
  M[12][2] = (Z[151]*Z[50]-Z[154]*Z[1])*Z[63];
  M[12][3] = -(Z[157]*Z[1]+Z[160]*Z[73])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M13()
{
  M[13][0] = -(Z[127]*Z[77]+Z[130]*Z[81])*Z[21];
  M[13][1] = -(Z[163]*Z[22]+Z[169]*Z[31])*Z[49];
  M[13][2] = (Z[151]*Z[107]-Z[154]*Z[77])*Z[63];
  M[13][3] = -(Z[157]*Z[77]+Z[160]*Z[110])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M18()
{
  M[18][0] = -(Z[8]*Z[119]+Z[14]*Z[197])*Z[21];
  M[18][1] = -(Z[26]*Z[201]-Z[43]*Z[202])*Z[49];
  M[18][2] = (Z[114]*Z[184]-Z[118]*Z[119])*Z[63];
  M[18][3] = -(Z[188]*Z[119]+Z[193]*Z[121])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M19()
{
  M[19][0] = -(Z[8]*Z[122]+Z[14]*Z[204])*Z[21];
  M[19][1] = -(Z[86]*Z[201]-Z[102]*Z[202])*Z[49];
  M[19][2] = (Z[114]*Z[194]-Z[118]*Z[122])*Z[63];
  M[19][3] = -(Z[188]*Z[122]+Z[193]*Z[124])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M30()
{
  M[30][0] = -(Z[127]*Z[119]+Z[130]*Z[199])*Z[21];
  M[30][1] = -(Z[133]*Z[201]-Z[145]*Z[202])*Z[49];
  M[30][2] = (Z[181]*Z[185]-Z[183]*Z[119])*Z[63];
  M[30][3] = -(Z[209]*Z[119]+Z[212]*Z[120])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M31()
{
  M[31][0] = -(Z[127]*Z[122]+Z[130]*Z[206])*Z[21];
  M[31][1] = -(Z[163]*Z[201]-Z[175]*Z[202])*Z[49];
  M[31][2] = (Z[181]*Z[195]-Z[183]*Z[122])*Z[63];
  M[31][3] = -(Z[209]*Z[122]+Z[212]*Z[123])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M32()
{
  M[32][0] = -(Z[215]*Z[9]+Z[220]*Z[18])*Z[21];
  M[32][1] = -(Z[30]*Z[22]-Z[47]*Z[221])*Z[49];
  M[32][2] = (Z[56]*Z[223]-Z[60]*Z[9])*Z[63];
  M[32][3] = -(Z[67]*Z[9]+Z[72]*Z[224])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M33()
{
  M[33][0] = -(Z[215]*Z[78]+Z[220]*Z[82])*Z[21];
  M[33][1] = -(Z[90]*Z[22]-Z[106]*Z[221])*Z[49];
  M[33][2] = (Z[56]*Z[227]-Z[60]*Z[78])*Z[63];
  M[33][3] = -(Z[67]*Z[78]+Z[72]*Z[228])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M44()
{
  M[44][0] = -(Z[235]*Z[9]+Z[238]*Z[15])*Z[21];
  M[44][1] = -(Z[136]*Z[22]-Z[148]*Z[221])*Z[49];
  M[44][2] = (Z[151]*Z[222]-Z[154]*Z[9])*Z[63];
  M[44][3] = -(Z[157]*Z[9]+Z[160]*Z[225])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M45()
{
  M[45][0] = -(Z[235]*Z[78]+Z[238]*Z[80])*Z[21];
  M[45][1] = -(Z[166]*Z[22]-Z[178]*Z[221])*Z[49];
  M[45][2] = (Z[151]*Z[226]-Z[154]*Z[78])*Z[63];
  M[45][3] = -(Z[157]*Z[78]+Z[160]*Z[229])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M50()
{
  M[50][0] = -(Z[215]*Z[196]+Z[220]*Z[200])*Z[21];
  M[50][1] = -(Z[30]*Z[201]+Z[39]*Z[243])*Z[49];
  M[50][2] = (Z[114]*Z[239]-Z[118]*Z[196])*Z[63];
  M[50][3] = -(Z[188]*Z[196]+Z[193]*Z[231])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M51()
{
  M[51][0] = -(Z[215]*Z[203]+Z[220]*Z[207])*Z[21];
  M[51][1] = -(Z[90]*Z[201]+Z[98]*Z[243])*Z[49];
  M[51][2] = (Z[114]*Z[241]-Z[118]*Z[203])*Z[63];
  M[51][3] = -(Z[188]*Z[203]+Z[193]*Z[233])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M62()
{
  M[62][0] = -(Z[235]*Z[196]+Z[238]*Z[198])*Z[21];
  M[62][1] = -(Z[136]*Z[201]+Z[142]*Z[243])*Z[49];
  M[62][2] = (Z[181]*Z[240]-Z[183]*Z[196])*Z[63];
  M[62][3] = -(Z[209]*Z[196]+Z[212]*Z[230])*Z[76];
}

void V2_4__sb__db__em__ep__db__sb::Calculate_M63()
{
  M[63][0] = -(Z[235]*Z[203]+Z[238]*Z[205])*Z[21];
  M[63][1] = -(Z[166]*Z[201]+Z[172]*Z[243])*Z[49];
  M[63][2] = (Z[181]*Z[242]-Z[183]*Z[203])*Z[63];
  M[63][3] = -(Z[209]*Z[203]+Z[212]*Z[232])*Z[76];
}

