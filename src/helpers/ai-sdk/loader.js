import { Source } from "./Source";


/*Prevents globalThis being reported as an error by eslint*/
/*global globalThis*/

// Singleton
let aiSdkInstance;
let source;

async function downloadAiSdk() {
  if (globalThis.CY) {
    throw new Error("AI-SDK has already been downloaded.");
  }
}

async function initAiSdk() {
  if (aiSdkInstance) {
    throw new Error("An instance of the AI-SDK is already running.");
  }
  source = new Source();

  aiSdkInstance = await globalThis.CY.loader()
    // TODO INSERT YOUR LICENSE KEY HERE
    .licenseKey("sk5f9dbc10476c4e636fafc83f4e4129fd40b3f4bdf2f7") // <--- ##############
    .source(source)
    .addModule(globalThis.CY.modules().FACE_DETECTOR.name)
    .addModule(globalThis.CY.modules().FACE_EMOTION.name, {
      enableBalancer: false, // example of custom setting
      smoothness: 0.5,
    })
    .addModule(globalThis.CY.modules().FACE_AROUSAL_VALENCE.name, {
      smoothness: 0.9, // example of custom setting
    })
    .addModule(globalThis.CY.modules().FACE_ATTENTION.name, {})
    .addModule(globalThis.CY.modules().DATA_AGGREGATOR.name, {})
    .load();
}

/**
 * Loads the MorphCast SDK, only the first time, then returns the controls for the start / stop
 *
 * @returns {Promise<{getModule: *, stop: *, CY: *, start: *, source: *}>}
 */
export async function getAiSdkControls() {
  if (globalThis.CY === undefined) {
    await downloadAiSdk();
  }
  if (aiSdkInstance === undefined) {
    await initAiSdk();
  }

  const { start, stop, getModule } = aiSdkInstance;
  return { start, stop, getModule, source, CY: globalThis.CY };
}
