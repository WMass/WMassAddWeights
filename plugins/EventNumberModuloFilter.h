#ifndef EventNumberModuloFilter_h
#define EventNumberModuloFilter_h
// -*- C++ -*-
//
// Package:    EventNumberModuloFilter
// Class:      EventNumberModuloFilter
//
/**\class EventNumberModuloFilter EventNumberModuloFilter.cc filter/EventNumberModuloFilter/src/EventNumberModuloFilter.cc

Description: Filter to select HCAL abort gap events

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Martin Grunewald
//         Created:  Tue Jan 22 13:55:00 CET 2008
//
//

// include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include <string>

namespace edm {
  class ConfigurationDescriptions;
}

//
// class declaration
//

class EventNumberModuloFilter : public edm::EDFilter {
public:
  explicit EventNumberModuloFilter(const edm::ParameterSet&);
  ~EventNumberModuloFilter() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  bool filter(edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------

  /// accept the event if its event number is a multiple of period_
  unsigned int period_;
  unsigned int remainder_;
  /// if invert_=true, invert that event accept decision
  bool invert_;
};

#endif
