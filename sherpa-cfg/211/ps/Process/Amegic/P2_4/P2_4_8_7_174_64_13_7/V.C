#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_4_8_7_174_64_13_7(Basic_Sfuncs* bs) {
  return new VP2_4_8_7_174_64_13_7(bs);
}

VP2_4_8_7_174_64_13_7::VP2_4_8_7_174_64_13_7(Basic_Sfuncs* _BS) :
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

VP2_4_8_7_174_64_13_7::~VP2_4_8_7_174_64_13_7()
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

Complex VP2_4_8_7_174_64_13_7::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 12: Calculate_M12(); break;
    case 18: Calculate_M18(); break;
    case 30: Calculate_M30(); break;
    case 33: Calculate_M33(); break;
    case 45: Calculate_M45(); break;
    case 51: Calculate_M51(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void VP2_4_8_7_174_64_13_7::Calculate_M0()
{
  M[0][0] = -(Z[8]*Z[1]+Z[13]*Z[9])*Z[18];
  M[0][1] = -(Z[23]*Z[19]+Z[28]*Z[24])*Z[34];
  M[0][2] = (Z[41]*Z[37]-Z[45]*Z[1])*Z[48];
  M[0][3] = -(Z[52]*Z[1]+Z[57]*Z[53])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M12()
{
  M[12][0] = -(Z[90]*Z[1]+Z[93]*Z[14])*Z[18];
  M[12][1] = -(Z[96]*Z[19]+Z[99]*Z[24])*Z[34];
  M[12][2] = (Z[105]*Z[35]-Z[108]*Z[1])*Z[48];
  M[12][3] = -(Z[111]*Z[1]+Z[114]*Z[58])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M18()
{
  M[18][0] = -(Z[8]*Z[85]+Z[13]*Z[139])*Z[18];
  M[18][1] = -(Z[23]*Z[141]-Z[32]*Z[142])*Z[34];
  M[18][2] = (Z[80]*Z[129]-Z[84]*Z[85])*Z[48];
  M[18][3] = -(Z[133]*Z[85]+Z[138]*Z[87])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M30()
{
  M[30][0] = -(Z[90]*Z[85]+Z[93]*Z[140])*Z[18];
  M[30][1] = -(Z[96]*Z[141]-Z[102]*Z[142])*Z[34];
  M[30][2] = (Z[126]*Z[130]-Z[128]*Z[85])*Z[48];
  M[30][3] = -(Z[147]*Z[85]+Z[150]*Z[86])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M33()
{
  M[33][0] = -(Z[153]*Z[62]+Z[158]*Z[64])*Z[18];
  M[33][1] = -(Z[68]*Z[19]-Z[76]*Z[159])*Z[34];
  M[33][2] = (Z[41]*Z[161]-Z[45]*Z[62])*Z[48];
  M[33][3] = -(Z[52]*Z[62]+Z[57]*Z[162])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M45()
{
  M[45][0] = -(Z[167]*Z[62]+Z[170]*Z[63])*Z[18];
  M[45][1] = -(Z[117]*Z[19]-Z[123]*Z[159])*Z[34];
  M[45][2] = (Z[105]*Z[160]-Z[108]*Z[62])*Z[48];
  M[45][3] = -(Z[111]*Z[62]+Z[114]*Z[163])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M51()
{
  M[51][0] = -(Z[153]*Z[143]+Z[158]*Z[145])*Z[18];
  M[51][1] = -(Z[68]*Z[141]+Z[72]*Z[173])*Z[34];
  M[51][2] = (Z[80]*Z[171]-Z[84]*Z[143])*Z[48];
  M[51][3] = -(Z[133]*Z[143]+Z[138]*Z[165])*Z[61];
}

void VP2_4_8_7_174_64_13_7::Calculate_M63()
{
  M[63][0] = -(Z[167]*Z[143]+Z[170]*Z[144])*Z[18];
  M[63][1] = -(Z[117]*Z[141]+Z[120]*Z[173])*Z[34];
  M[63][2] = (Z[126]*Z[172]-Z[128]*Z[143])*Z[48];
  M[63][3] = -(Z[147]*Z[143]+Z[150]*Z[164])*Z[61];
}

