#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__G__db__em__ep__db__S1_0(Basic_Sfuncs* bs) {
  return new V2_3__G__db__em__ep__db__S1_0(bs);
}

V2_3__G__db__em__ep__db__S1_0::V2_3__G__db__em__ep__db__S1_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[88];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

V2_3__G__db__em__ep__db__S1_0::~V2_3__G__db__em__ep__db__S1_0()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<32;i++) delete[] M[i];
    delete[] M;
  }
}

Complex V2_3__G__db__em__ep__db__S1_0::Evaluate(int m,int n)
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
  }
  cl[n]=1;
  return M[n][m];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M0()
{
  M[0][0] = -(Z[18]*Z[17]-Z[8]*Z[7])*Z[19];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M1()
{
  M[1][0] = -Z[19]*Z[30]*Z[17];
  M[1][1] = -Z[28]*Z[31]*Z[23];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M2()
{
  M[2][0] = (Z[13]*Z[40]+Z[8]*Z[36])*Z[19];
  M[2][1] = -(Z[46]*Z[27]+Z[45]*Z[23])*Z[28];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M3()
{
  M[3][0] = Z[19]*Z[29]*Z[40];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M12()
{
  M[12][0] = -(Z[18]*Z[55]-Z[8]*Z[49])*Z[19];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M13()
{
  M[13][0] = -Z[19]*Z[30]*Z[55];
  M[13][1] = -Z[28]*Z[31]*Z[58];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M14()
{
  M[14][0] = (Z[13]*Z[67]+Z[8]*Z[64])*Z[19];
  M[14][1] = -(Z[46]*Z[61]+Z[45]*Z[58])*Z[28];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M15()
{
  M[15][0] = Z[19]*Z[29]*Z[67];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M16()
{
  M[16][0] = Z[19]*Z[71]*Z[7];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M17()
{
  M[17][0] = (Z[81]*Z[12]+Z[80]*Z[7])*Z[19];
  M[17][1] = -(Z[32]*Z[79]+Z[31]*Z[75])*Z[28];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M18()
{
  M[18][0] = -Z[19]*Z[18]*Z[44];
  M[18][1] = -Z[28]*Z[46]*Z[79];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M19()
{
  M[19][0] = -(Z[30]*Z[44]-Z[81]*Z[40])*Z[19];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M28()
{
  M[28][0] = Z[19]*Z[71]*Z[49];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M29()
{
  M[29][0] = (Z[81]*Z[52]+Z[80]*Z[49])*Z[19];
  M[29][1] = -(Z[32]*Z[87]+Z[31]*Z[84])*Z[28];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M30()
{
  M[30][0] = -Z[19]*Z[18]*Z[70];
  M[30][1] = -Z[28]*Z[46]*Z[87];
}

void V2_3__G__db__em__ep__db__S1_0::Calculate_M31()
{
  M[31][0] = -(Z[30]*Z[70]-Z[81]*Z[67])*Z[19];
}

