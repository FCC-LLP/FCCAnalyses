// -*- C++ -*-
//
/** FCCAnalysis module: ExoticHiggsDecays_analysis_code
 *
 * \file ExoticHiggsDecays_analysis_code.h
 * \author <mvoorde> <<m.voorde96@gmail.com>>
 *
 * Description:
 *   [...]
 */

#ifndef ExoticHiggsDecays_analysis_code_ExoticHiggsDecays_analysis_code_h
#define ExoticHiggsDecays_analysis_code_ExoticHiggsDecays_analysis_code_h

#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticle.h"
#include "edm4hep/MCParticle.h"
#include "FCCAnalyses/MCParticle.h"

namespace ExoticHiggsDecays_analysis_code {
  namespace rv = ROOT::VecOps;

  void dummy_analysis();
  rv::RVec<float> dummy_collection(const rv::RVec<edm4hep::ReconstructedParticleData>&);

  ROOT::VecOps::RVec<float> get_both_scalars(ROOT::VecOps::RVec<float> scalar1_value, ROOT::VecOps::RVec<float> scalar2_value);

  struct selMC_leg{
    selMC_leg( int arg_idx );
    int m_idx;
    ROOT::VecOps::RVec<edm4hep::MCParticleData> operator() (ROOT::VecOps::RVec<int> list_of_indices,
							  ROOT::VecOps::RVec<edm4hep::MCParticleData> in) ;
  };
}  // end namespace ExoticHiggsDecays_analysis_code

#endif
