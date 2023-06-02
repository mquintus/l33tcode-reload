class EventEmitter {
  constructor() {
      this.callback_store = {};
      this.cb_counter = 0;
  }

  subscribe(event, cb) {
    const cb_counter = this.cb_counter;
    this.cb_counter = this.cb_counter + 1;

    if (!(event in this.callback_store)) {
        this.callback_store[event] = {};
    }
    
    this.callback_store[event][cb_counter] = cb;
    const that = this;

    return {
        unsubscribe: () => {
            if (event in that.callback_store) {
                 if (cb_counter in that.callback_store[event]) {
                      delete that.callback_store[event][cb_counter];
                 }
            }
            
        }
    };
  }

  emit(event, args = []) {
    var ret = [];
    if ((event in this.callback_store)) {
        for (var [ctr, cb] of Object.entries(this.callback_store[event])) {
            const ret_single = cb(...args);
            if (typeof ret_single == 'undefined') {
                continue;
            }
            if (ret_single === null) {
                continue;
            }
            ret.push(ret_single);
        }
    }
    return ret;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
