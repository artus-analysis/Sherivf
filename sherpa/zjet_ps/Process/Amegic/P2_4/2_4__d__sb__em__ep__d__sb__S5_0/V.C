#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__d__sb__em__ep__d__sb__S5_0(Basic_Sfuncs* bs) {
  return new V2_4__d__sb__em__ep__d__sb__S5_0(bs);
}

V2_4__d__sb__em__ep__d__sb__S5_0::V2_4__d__sb__em__ep__d__sb__S5_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[7];
  Z = new Complex[174];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__d__sb__em__ep__d__sb__S5_0::~V2_4__d__sb__em__ep__d__sb__S5_0()
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

Complex V2_4__d__sb__em__ep__d__sb__S5_0::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 12: Calculate_M12(); break;
    case 17: Calculate_M17(); break;
    case 29: Calculate_M29(); break;
    case 34: Calculate_M34(); break;
    case 46: Calculate_M46(); break;
    case 51: Calculate_M51(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M0()
{
  M[0][0] = (Z[17]*Z[13]-Z[12]*Z[8])*Z[20];
  M[0][1] = (Z[27]*Z[23]+Z[32]*Z[28])*Z[34];
  M[0][2] = (Z[41]*Z[37]-Z[45]*Z[28])*Z[48];
  M[0][3] = -(Z[52]*Z[28]+Z[57]*Z[53])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M12()
{
  M[12][0] = (Z[96]*Z[13]-Z[93]*Z[8])*Z[20];
  M[12][1] = (Z[99]*Z[21]+Z[102]*Z[28])*Z[34];
  M[12][2] = (Z[105]*Z[35]-Z[108]*Z[28])*Z[48];
  M[12][3] = -(Z[111]*Z[28]+Z[114]*Z[58])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M17()
{
  M[17][0] = (Z[65]*Z[129]+Z[73]*Z[13])*Z[20];
  M[17][1] = (Z[133]*Z[74]+Z[137]*Z[76])*Z[34];
  M[17][2] = (Z[41]*Z[139]-Z[45]*Z[76])*Z[48];
  M[17][3] = -(Z[52]*Z[76]+Z[57]*Z[140])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M29()
{
  M[29][0] = (Z[117]*Z[129]+Z[123]*Z[13])*Z[20];
  M[29][1] = (Z[147]*Z[75]+Z[149]*Z[76])*Z[34];
  M[29][2] = (Z[105]*Z[138]-Z[108]*Z[76])*Z[48];
  M[29][3] = -(Z[111]*Z[76]+Z[114]*Z[141])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M34()
{
  M[34][0] = (Z[7]*Z[160]+Z[17]*Z[161])*Z[20];
  M[34][1] = (Z[27]*Z[163]+Z[32]*Z[85])*Z[34];
  M[34][2] = (Z[80]*Z[150]-Z[84]*Z[85])*Z[48];
  M[34][3] = -(Z[154]*Z[85]+Z[159]*Z[87])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M46()
{
  M[46][0] = (Z[90]*Z[160]+Z[96]*Z[161])*Z[20];
  M[46][1] = (Z[99]*Z[162]+Z[102]*Z[85])*Z[34];
  M[46][2] = (Z[126]*Z[151]-Z[128]*Z[85])*Z[48];
  M[46][3] = -(Z[167]*Z[85]+Z[170]*Z[86])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M51()
{
  M[51][0] = (Z[73]*Z[161]-Z[69]*Z[173])*Z[20];
  M[51][1] = (Z[133]*Z[164]+Z[137]*Z[142])*Z[34];
  M[51][2] = (Z[80]*Z[171]-Z[84]*Z[142])*Z[48];
  M[51][3] = -(Z[154]*Z[142]+Z[159]*Z[144])*Z[61];
}

void V2_4__d__sb__em__ep__d__sb__S5_0::Calculate_M63()
{
  M[63][0] = (Z[123]*Z[161]-Z[120]*Z[173])*Z[20];
  M[63][1] = (Z[147]*Z[165]+Z[149]*Z[142])*Z[34];
  M[63][2] = (Z[126]*Z[172]-Z[128]*Z[142])*Z[48];
  M[63][3] = -(Z[167]*Z[142]+Z[170]*Z[143])*Z[61];
}

